# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpccs', '0002_auto_20170731_0151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etnia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'etnia',
                'ordering': ('nombre',),
            },
        ),
    ]