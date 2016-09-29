from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.response import TemplateResponse
from mymensor.models import Photo, AmazonSNSNotification
from mymensor.serializer import AmazonSNSNotificationSerializer
import json, requests
#from mymensor.forms import AssetOwnerConfigurationFormSet, AssetConfigurationFormSet, DciConfigurationFormSet

# Amazon SNS Notification Processor View
@csrf_exempt
def amazon_sns_processor(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        serializer = AmazonSNSNotificationSerializer(data=body)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=200)
    return HttpResponse(status=400)

#URL Redirect for OPENID Connect purposes
def oauth2redirect(request):
    return HttpResponse(request)

# Portfolio View
@login_required
def portfolio(request):
    photos = Photo.objects.all()
    return render(request, 'index.html', {'photos': photos,})


# Photo Feed View
@login_required
def photofeed(request):
    photos = Photo.objects.all()
    return render(request, 'photofeed.html', {'photos': photos,})


def zerossl(request):
    if request.method == "GET":
        return TemplateResponse(request, "temp.html")

def android_assetlinks(request):
    if request.method == "GET":
        return JsonResponse([{  "relation": ["delegate_permission/common.handle_all_urls"],
                                "target" : { "namespace": "android_app", "package_name": "net.openid.appauthdemo",
                                            "sha256_cert_fingerprints": ["D7:6C:37:83:CC:EA:40:CD:F5:4C:95:69:07:90:93:E6:2E:D9:78:04:24:79:57:5E:6D:9D:50:98:13:66:4C:B1"] }
}])

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
