from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.response import TemplateResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from instant.producers import broadcast
from mymensor.models import Asset, Vp, Media, AmazonS3Message, AmazonSNSNotification
from mymensor.serializer import AmazonSNSNotificationSerializer
from mymensorapp.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_S3_BUCKET_NAME, AWS_DEFAULT_REGION
import json, boto3
import dateutil.parser
import dateutil.relativedelta
from datetime import *

#from mymensor.forms import AssetOwnerConfigurationFormSet, AssetConfigurationFormSet, DciConfigurationFormSet


# Amazon SNS Notification Processor View
@csrf_exempt
def amazon_sns_processor(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        serializer = AmazonSNSNotificationSerializer(data=body)
        if serializer.is_valid():
            amzSns = AmazonSNSNotification(**serializer.validated_data)
            amzSns.save()
            message_json = json.loads(body['Message'])
            amzs3msg = AmazonS3Message()
            amzs3msg.amazonSNSNotification = amzSns
            message_items = message_json['Records'][0]
            amzs3msg.eventVersion = message_items['eventVersion']
            amzs3msg.eventSource = message_items['eventSource']
            amzs3msg.awsRegion = message_items['awsRegion']
            amzs3msg.eventTime = message_items['eventTime']
            amzs3msg.eventName = message_items['eventName']
            amzs3msg.userIdentity_principalId = message_items['userIdentity']['principalId']
            amzs3msg.requestParameters_sourceIPAddress = message_items['requestParameters']['sourceIPAddress']
            amzs3msg.responseElements_x_amz_request_id = message_items['responseElements']['x-amz-request-id']
            amzs3msg.responseElements_x_amz_id_2 = message_items['responseElements']['x-amz-id-2']
            amzs3msg.s3_s3SchemaVersion = message_items['s3']['s3SchemaVersion']
            amzs3msg.s3_configurationId = message_items['s3']['configurationId']
            amzs3msg.s3_bucket_name = message_items['s3']['bucket']['name']
            amzs3msg.s3_bucket_arn = message_items['s3']['bucket']['arn']
            amzs3msg.s3_bucket_ownerIdentity_principalId = message_items['s3']['bucket']['ownerIdentity']['principalId']
            amzs3msg.s3_object_key = message_items['s3']['object']['key']
            amzs3msg.s3_object_size = message_items['s3']['object']['size']
            amzs3msg.s3_object_eTag = message_items['s3']['object']['eTag']
            amzs3msg.s3_object_versionId = message_items['s3']['object']['versionId']
            amzs3msg.s3_object_sequencer = message_items['s3']['object']['sequencer']
            amzs3msg.save()

            session = boto3.session.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
            s3 = session.resource('s3')
            object = s3.Object(amzs3msg.s3_bucket_name,amzs3msg.s3_object_key)
            object.load()
            obj_metadata = object.metadata
            media_received = Media()
            media_received.amazonS3Message = amzs3msg
            media_received.mediaMillisSinceEpoch = obj_metadata['phototakenmillis']
            media_received.mediaVpNumber = obj_metadata['vp']
            media_received.mediaMymensorAccount = obj_metadata['mymensoraccount']

            # Fetching the info necessary to fill the vp_id i.e. pk information
            media_user_id = User.objects.get(username=media_received.mediaMymensorAccount).pk
            media_asset_id = Asset.objects.get(assetOwner=media_user_id).pk
            media_received.vp = Vp.objects.get(asset=media_asset_id, vpNumber=media_received.mediaVpNumber)
            media_received.mediaAssetNumber = Asset.objects.get(pk=media_asset_id).assetNumber
            media_received.mediaObjectS3Key = amzs3msg.s3_object_key
            media_received.mediaContentType = object.content_type
            media_received.mediaSha256 = obj_metadata['sha-256']
            media_received.mediaLatitude = obj_metadata['loclatitude']
            media_received.mediaLongitude = obj_metadata['loclongitude']
            media_received.mediaAltitude = obj_metadata['localtitude']
            media_received.mediaLocPrecisionInMeters = obj_metadata['locprecisioninm']
            media_received.mediaLocMethod = obj_metadata['locmethod']
            media_received.mediaLocMillis = obj_metadata['locmillis']
            media_received.mediaLocIsCertified = obj_metadata['loccertified']
            media_received.mediaTimeIsCertified = obj_metadata['timecertified']
            media_received.mediaArIsOn = obj_metadata['isarswitchon']
            media_received.mediaTimeStamp = obj_metadata['datetime']

            # Presently the Mobile App DOES NOT PROCESS the VPs
            media_received.mediaProcessed = False

            media_received.save()

            broadcast(message='New media arrived on server', event_class="NewMedia", data={"username":media_received.mediaMymensorAccount})

            return HttpResponse(status=200)
    return HttpResponse(status=400)


# Portfolio View
@login_required
def portfolio(request):
    if request.user.is_authenticated:
        session = boto3.session.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        s3Client = session.client('s3')
        startdate = datetime.strptime(request.GET.get('startdate',(datetime.today()-dateutil.relativedelta.relativedelta(months=-1)).strftime('%Y-%m-%d')), '%Y-%m-%d')
        enddate = datetime.strptime(request.GET.get('enddate',datetime.today().strftime('%Y-%m-%d')), '%Y-%m-%d')
        new_enddate = enddate + dateutil.relativedelta.relativedelta(days=1)
        vps = Vp.objects.filter(asset__assetOwner=request.user).order_by('vpNumber')
        medias = Media.objects.filter(vp__asset__assetOwner=request.user).order_by('-mediaTimeStamp').order_by('mediaVpNumber')
        for media in medias:
            media.mediaStorageURL = s3Client.generate_presigned_url('get_object',
                                    Params={'Bucket': AWS_S3_BUCKET_NAME,'Key': media.mediaObjectS3Key},
                                    ExpiresIn=3600)
        return render(request, 'index.html', {'medias': medias, 'vps': vps, 'startdate':startdate, 'enddate':new_enddate}, status=200)


# Media Feed View
@login_required
def mediafeed(request):
    if request.user.is_authenticated:
        session = boto3.session.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        s3Client = session.client('s3')
        medias = Media.objects.filter(vp__asset__assetOwner=request.user).order_by('-mediaTimeStamp')[:50]
        vps = Vp.objects.filter(asset__assetOwner=request.user).order_by('vpNumber')
        for media in medias:
            media.mediaStorageURL = s3Client.generate_presigned_url('get_object',
                                    Params={'Bucket': AWS_S3_BUCKET_NAME,'Key': media.mediaObjectS3Key},
                                    ExpiresIn=3600)
        return render(request, 'mediafeed.html', {'medias': medias, 'vps': vps})


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def cognitoauth(request):
    if request.method == "GET":

        client = boto3.client(
            'cognito-identity',
            'eu-west-1',
            aws_access_key_id = AWS_ACCESS_KEY_ID,
            aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
            )

        token = (Token.objects.get(user_id = request.user.id)).key

        email = request.user.email

        response = client.get_open_id_token_for_developer_identity(
            IdentityPoolId='eu-west-1:963bc158-d9dd-4ae2-8279-b5a8b1524f73',
            Logins={
                'cogdevserv.mymensor.com': email
            },
            TokenDuration=600
        )
        response.update({'identityPoolId':'eu-west-1:963bc158-d9dd-4ae2-8279-b5a8b1524f73'})
        response.update({'key': token})
        return JsonResponse(response)
    return HttpResponse(status=400)


def zerossl(request):
    if request.method == "GET":
        return TemplateResponse(request, "zerossl.html")


def android_assetlinks(request):
    if request.method == "GET":
        return TemplateResponse(request, "android_assetlinks.html", content_type="application/json")


# Setup Side View
@login_required
def myMensorSetupFormView(request):
    pass
    #if request.method == 'POST':
        #assetOwnerFormSet = AssetOwnerConfigurationFormSet(request.POST, request.FILES, prefix='assetOwnerFormSet')
        #assetFormSet = AssetConfigurationFormSet(request.POST, request.FILES, prefix='assetFormSet')
        #dciFormSet = DciConfigurationFormSet(request.POST, request.FILES, prefix='dciFormSet')
        #if assetOwnerFormSet.is_valid() and assetFormSet.is_valid() and dciFormSet.is_valid():
        #    assetOwnerFormSet.save()
        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
    #else:
        #assetOwnerFormSet = AssetOwnerConfigurationFormSet(prefix='assetOwnerFormSet')
        #dciFormSet = DciConfigurationFormSet()
        #assetFormSet = AssetConfigurationFormSet()
    #return render(request, 'setup.html', {'formSetAssetOwner': assetOwnerFormSet, 'formSetAsset': assetFormSet, 'formSetDci':dciFormSet})
