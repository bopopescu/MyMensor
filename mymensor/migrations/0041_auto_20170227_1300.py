# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymensor', '0040_auto_20170227_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='assetDciFrequencyUnit',
            field=models.CharField(choices=[('millis', 'millis'), ('hour', 'hour'), ('day', 'day'), ('week', 'week'), ('month', 'month')], default='millis', max_length=50, verbose_name='Capture frequency unit'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tagDescription',
            field=models.CharField(max_length=1024, verbose_name='tag description'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tagExpValue',
            field=models.FloatField(null=True, verbose_name='expected value for the tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tagHighRed',
            field=models.FloatField(null=True, verbose_name='maximum value from which the tag will be flagged as in HIGH RED state'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tagHighYellow',
            field=models.FloatField(null=True, verbose_name='maximum value from which the tag will be flagged as in HIGH YELLOW state'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tagIsActive',
            field=models.BooleanField(default=True, verbose_name='tag is active'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tagLowRed',
            field=models.FloatField(null=True, verbose_name='minimum value from which the tag will be flagged as in LOW RED state'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tagLowYellow',
            field=models.FloatField(null=True, verbose_name='minimum value from which the tag will be flagged as in LOW YELLOW state'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tagQuestion',
            field=models.CharField(max_length=1024, verbose_name='question that shall be answered when processing this tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tagUnit',
            field=models.CharField(max_length=50, null=True, verbose_name='unit to be used when processing this tag'),
        ),
        migrations.AlterField(
            model_name='vp',
            name='vpDescription',
            field=models.CharField(max_length=1024, verbose_name='vp description'),
        ),
        migrations.AlterField(
            model_name='vp',
            name='vpFrequencyUnit',
            field=models.CharField(choices=[('millis', 'millis'), ('hour', 'hour'), ('day', 'day'), ('week', 'week'), ('month', 'month')], max_length=50, null=True, verbose_name='unit for the vp capture frequency'),
        ),
        migrations.AlterField(
            model_name='vp',
            name='vpFrequencyValue',
            field=models.IntegerField(null=True, verbose_name='vp capture frequency'),
        ),
    ]