# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-27 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymensor', '0050_auto_20170414_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vp',
            name='vpShareEmail',
            field=models.EmailField(default=None, max_length=254, null=True, verbose_name='send all of this vp captures to the following email.'),
        ),
    ]
