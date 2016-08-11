# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-11 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photoMillisSinceEpoch', models.BigIntegerField()),
                ('photoVpNumber', models.IntegerField()),
                ('photoAssetOwnerNumber', models.IntegerField()),
                ('photoAssetNumber', models.IntegerField()),
                ('photoStorageURL', models.CharField(max_length=255)),
                ('photoImageLatitude', models.FloatField()),
                ('photoImageLongitude', models.FloatField()),
                ('photoDBTimeStamp', models.DateTimeField(auto_now=True)),
                ('photoTimeStamp', models.DateTimeField()),
                ('photoProcessed', models.NullBooleanField()),
            ],
        ),
    ]
