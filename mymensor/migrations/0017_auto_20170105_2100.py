# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-05 21:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mymensor', '0016_auto_20170105_1930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amazonsnsnotification',
            old_name='s3_object_key',
            new_name='Message',
        ),
    ]
