# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-03 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymensor', '0084_vp_vpisused'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='mediaClientType',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
