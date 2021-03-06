# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-25 23:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpccs', '0004_auto_20171025_0724'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tiporequerimiento',
            options={'ordering': ('nombre',)},
        ),
        migrations.RenameField(
            model_name='requerimiento',
            old_name='indetificacion_id',
            new_name='identificacion_id',
        ),
        migrations.AlterField(
            model_name='requerimiento',
            name='tipodenuncia',
            field=models.ForeignKey(db_column='tipo_requerimiento_id', on_delete=django.db.models.deletion.CASCADE, related_name='tiporequerimientoid', to='cpccs.TipoRequerimiento'),
        ),
    ]
