# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymensor', '0041_auto_20170227_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='mediaDBTimeStamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='mobilesetupbackup',
            name='backupDBTimeStamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='processedtag',
            name='valValueEvaluatedEntryDBTimeStamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tagstatustable',
            name='statusDBTimeStamp',
            field=models.DateTimeField(auto_now=True, verbose_name='Processing Time'),
        ),
        migrations.AlterField(
            model_name='value',
            name='valValueEntryDBTimeStamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]