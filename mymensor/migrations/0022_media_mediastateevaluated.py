# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymensor', '0021_auto_20170109_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='mediaStateEvaluated',
            field=models.IntegerField(null=True),
        ),
    ]
