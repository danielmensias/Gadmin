# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-10 04:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='imagen_animal',
            field=models.ImageField(blank=True, default='siluetavaca.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='animal',
            name='peso_inicial',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
