# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('1', 'Pedido recebido'), ('2', 'Pedido em preparação'), ('3', 'Pedido saiu para entrega')], default=1, max_length=50, verbose_name='status do pedido'),
            preserve_default=False,
        ),
    ]
