# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpccs', '0009_remove_evidencia_denuncia'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidencia',
            name='denuncia',
            field=models.CharField(default=-1, max_length=255),
            preserve_default=False,
        ),
    ]
