# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-27 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymensor', '0070_auto_20170627_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='braintreesubscription',
            name='braintreesubscriptionCancelResultObject',
            field=models.CharField(max_length=32768, null=True),
        ),
    ]
