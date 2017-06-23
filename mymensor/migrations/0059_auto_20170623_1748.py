# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-23 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mymensor', '0058_auto_20170623_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyMPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mympricePlanName', models.CharField(max_length=1024)),
                ('mympriceBraintreePlanID', models.CharField(max_length=1024)),
                ('mympriceClientType', models.CharField(max_length=1024)),
                ('mympriceCurrency', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('BRL', 'BRL')], max_length=4)),
                ('mympriceNumericalValue', models.FloatField()),
                ('mympriceBillingCycleQty', models.IntegerField()),
                ('mympriceBillingCycleUnit', models.CharField(max_length=255)),
                ('mympriceBillingExpirationExists', models.BooleanField(default=False)),
                ('mympriceBillingExpirationInCycleQty', models.IntegerField(null=True)),
                ('mympriceDiscountExists', models.BooleanField(default=False)),
                ('mympriceDiscountPercentage', models.FloatField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='assetMyMPrice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mymensor.MyMPrice'),
        ),
    ]
