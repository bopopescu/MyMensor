# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-27 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymensor', '0069_auto_20170625_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='assetDateOfEndEfTrialBeforeSubscription',
            field=models.DateTimeField(null=True, verbose_name='End of Trial Befor Subscription'),
        ),
        migrations.AddField(
            model_name='braintreesubscription',
            name='braintreesubscriptionLastDay',
            field=models.DateTimeField(null=True),
        ),
    ]
