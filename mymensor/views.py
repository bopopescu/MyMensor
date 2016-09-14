from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from mymensor.models import Photo, Asset
from mymensor.serializer import AmazonSNSNotificationSerializer
#from mymensor.forms import AssetOwnerConfigurationFormSet, AssetConfigurationFormSet, DciConfigurationFormSet

# Amazon SNS Notification Processor View
def amazon_sns_processor(request):
    if request.method == "POST":
        serializer = AmazonSNSNotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
