# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 11:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('misLineas', '0007_pago_verificado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linea',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]