# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-26 04:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_reproduccion_id_animal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventosanitario',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]
