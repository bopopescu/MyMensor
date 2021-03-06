# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 20:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mymensor', '0046_auto_20170331_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fbUserId', models.CharField(max_length=1024, null=True, verbose_name='Facebook User ID')),
                ('fbUserName', models.CharField(max_length=1024, null=True, verbose_name='Facebook User Name')),
                ('fbShortTermAccesToken', models.CharField(max_length=2048, null=True, verbose_name='Facebook Short Term Access Token')),
                ('fbShortTermAccesTokenIssuedAt', models.DateTimeField(null=True, verbose_name='Facebook Short Term Access Token Issue Time')),
                ('fbShortTermAccesTokenSignedRequest', models.CharField(max_length=2048, null=True, verbose_name='Facebook Short Term Access Token Signed Request')),
                ('fbLongTermAccesToken', models.CharField(max_length=2048, null=True, verbose_name='Facebook Short Term Access Token')),
                ('fbLongTermAccesTokenIssuedAt', models.DateTimeField(null=True, verbose_name='Facebook Short Term Access Token Issue Time')),
                ('fbOwner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Facebook Owner')),
            ],
        ),
    ]
