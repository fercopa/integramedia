# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misLineas', '0002_auto_20160618_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='asunto',
            field=models.IntegerField(choices=[(1, 'Pago realizado'), (2, 'Cambio de abono'), (3, 'Actualizar datos'), (4, 'Otros...')], default=1),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='medio',
            field=models.IntegerField(choices=[(1, 'Via SMS'), (2, 'Via e-mail')], default=1),
        ),
    ]
