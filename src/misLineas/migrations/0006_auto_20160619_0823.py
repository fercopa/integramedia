# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 08:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misLineas', '0005_auto_20160618_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='texto',
            new_name='mensaje',
        ),
    ]