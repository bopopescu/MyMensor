# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mymensor', '0027_tagstatustable'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagstatustable',
            name='statusDBTimeStamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
