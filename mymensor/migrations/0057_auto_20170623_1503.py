# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-23 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymensor', '0056_braintreecustomer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='braintreecustomer',
            name='braintreecustomerMerchantAccId',
            field=models.CharField(choices=[('mymensorUSD', 'USD'), ('mymensorEUR', 'EUR'), ('mymensorBRL', 'BRL')], default='mymensorUSD', max_length=1024, verbose_name='Current currentcy in use'),
        ),
    ]
