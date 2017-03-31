# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymensor', '0045_auto_20170331_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tagExpValue',
            field=models.FloatField(blank=True, null=True, verbose_name='expected value for the tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tagHighRed',
            field=models.FloatField(blank=True, null=True, verbose_name='maximum value from which the tag will be flagged as in HIGH RED state'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tagHighYellow',
            field=models.FloatField(blank=True, null=True, verbose_name='maximum value from which the tag will be flagged as in HIGH YELLOW state'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tagLowRed',
            field=models.FloatField(blank=True, null=True, verbose_name='minimum value from which the tag will be flagged as in LOW RED state'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tagLowYellow',
            field=models.FloatField(blank=True, null=True, verbose_name='minimum value from which the tag will be flagged as in LOW YELLOW state'),
        ),
    ]
