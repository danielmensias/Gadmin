# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-02 06:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animales', '0001_initial'),
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reproduccion',
            name='id_animal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='animales.Animal'),
            preserve_default=False,
        ),
    ]
