# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misLineas', '0011_auto_20160619_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linea',
            name='plan',
            field=models.IntegerField(blank=True, choices=[(1, 'Economicoi $90'), (2, 'Normal $150'), (3, 'Premium $350')], default=1, null=True),
        ),
    ]
