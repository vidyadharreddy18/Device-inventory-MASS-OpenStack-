# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appserver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dev_info',
            name='info_type',
            field=models.CharField(default='devices', max_length=100),
        ),
    ]
