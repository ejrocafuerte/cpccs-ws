# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpccs', '0006_auto_20170801_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predenuncia',
            name='descripcioninvestigacion',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='predenuncia',
            name='funcionariopublico',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='predenuncia',
            name='generodenunciado',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='predenuncia',
            name='generodenunciante',
            field=models.CharField(max_length=255),
        ),
    ]