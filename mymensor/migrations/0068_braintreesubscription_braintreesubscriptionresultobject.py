# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-25 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymensor', '0067_braintreesubscription_braintreesubscriptionpaymentinstrumenttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='braintreesubscription',
            name='braintreesubscriptionResultObject',
            field=models.CharField(max_length=32768, null=True),
        ),
    ]
