# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misLineas', '0013_auto_20160620_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='linea',
            name='solicitud_de_alta',
            field=models.BooleanField(default=False),
        ),
    ]
