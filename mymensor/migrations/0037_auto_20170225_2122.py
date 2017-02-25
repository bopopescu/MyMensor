# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymensor', '0036_auto_20170223_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processedtag',
            name='tagStateEvaluated',
            field=models.CharField(choices=[('NP', 'NOT PROCESSED'), ('PR', 'PROCESSED'), ('LR', 'LOW RED'), ('LY', 'LOW YELLOW'), ('GR', 'GREEN'), ('HY', 'HIGH YELLOW'), ('HR', 'HIGH RED')], max_length=50),
        ),
        migrations.AlterField(
            model_name='value',
            name='tagStateResultingFromValValueStatus',
            field=models.CharField(choices=[('NP', 'NOT PROCESSED'), ('PR', 'PROCESSED'), ('LR', 'LOW RED'), ('LY', 'LOW YELLOW'), ('GR', 'GREEN'), ('HY', 'HIGH YELLOW'), ('HR', 'HIGH RED')], max_length=50),
        ),
    ]
