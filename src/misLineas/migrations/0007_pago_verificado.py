# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misLineas', '0006_auto_20160619_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='verificado',
            field=models.BooleanField(default=False),
        ),
    ]
