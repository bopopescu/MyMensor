# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-26 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mymensor', '0010_delete_openidouath2redirectcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mediaMillisSinceEpoch', models.BigIntegerField()),
                ('mediaVpNumber', models.IntegerField()),
                ('mediaAssetNumber', models.IntegerField()),
                ('mediaStorageURL', models.CharField(max_length=255)),
                ('mediaLatitude', models.FloatField()),
                ('mediaLongitude', models.FloatField()),
                ('mediaAltitude', models.FloatField()),
                ('mediaLocPrecisionInMeters', models.FloatField()),
                ('mediaLocMethod', models.CharField(max_length=255)),
                ('mediaLocMillis', models.BigIntegerField()),
                ('mediaSha256', models.CharField(max_length=1024, null=True)),
                ('mediaLocIsCertified', models.NullBooleanField()),
                ('mediaTimeIsCertified', models.NullBooleanField()),
                ('mediaArIsOn', models.NullBooleanField()),
                ('mediaDBTimeStamp', models.DateTimeField(auto_now_add=True)),
                ('mediaTimeStamp', models.DateTimeField()),
                ('mediaMymensorAccount', models.CharField(max_length=255)),
                ('mediaProcessed', models.NullBooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='photo',
            name='vp',
        ),
        migrations.RenameField(
            model_name='asset',
            old_name='dciTolerancePosition',
            new_name='assetDciTolerancePosition',
        ),
        migrations.RenameField(
            model_name='asset',
            old_name='dciToleranceRotation',
            new_name='assetDciToleranceRotation',
        ),
        migrations.RenameField(
            model_name='vp',
            old_name='vpIsSuperMultiple',
            new_name='vpArIsConfigured',
        ),
        migrations.RenameField(
            model_name='vp',
            old_name='vpSuperIdIsLarge',
            new_name='vpIsVideo',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='assetProviderAcc',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='assetProviderAccPassword',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='assetStoragePassword',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='dciConfigPassword',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='dciDciBoxWifiAdministrator',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='dciDciBoxWifiModel',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='dciDciBoxWifiPassword',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='dciDciBoxWifiSSID',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='dciFrequencyUnit',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='dciFrequencyValue',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='dciIMEI',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='dciModel',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='dciQtyVps',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='dciRemotePassword',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='dciUserPassword',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='dciWifiMAC',
        ),
        migrations.RemoveField(
            model_name='processedtag',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='vp',
            name='vpSuperIdIsMedium',
        ),
        migrations.RemoveField(
            model_name='vp',
            name='vpSuperIdIsSmall',
        ),
        migrations.AddField(
            model_name='asset',
            name='assetDciFrequencyUnit',
            field=models.CharField(default='millis', max_length=50),
        ),
        migrations.AddField(
            model_name='asset',
            name='assetDciFrequencyValue',
            field=models.IntegerField(default=20000),
        ),
        migrations.AddField(
            model_name='asset',
            name='assetDciQtyVps',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='vp',
            name='vpStdMarkerPhotoFileSize',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='vp',
            name='vpStdPhotoFileSize',
            field=models.BigIntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AddField(
            model_name='media',
            name='vp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mymensor.Vp'),
        ),
        migrations.AddField(
            model_name='processedtag',
            name='media',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mymensor.Media'),
            preserve_default=False,
        ),
    ]
