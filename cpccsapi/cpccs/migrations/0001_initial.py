# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-23 18:18
from __future__ import unicode_literals

import cpccs.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'ciudad',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('contenido', models.CharField(max_length=255)),
                ('url_video', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'contenido',
            },
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'estadocivil',
                'ordering': ('nombre',),
            },
        ),
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
        migrations.CreateModel(
            name='Evidencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denuncia', models.CharField(max_length=255)),
                ('fecha', models.DateField(auto_now=True)),
                ('archivo', models.FileField(upload_to=cpccs.models.make_dir)),
            ],
            options={
                'db_table': 'evidencia',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'estadocivil',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='NivelEducacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'niveleducacion',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'provincia',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Requerimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaIngreso', models.DateField(auto_now_add=True)),
                ('identidad_reservada', models.BooleanField(default=0)),
                ('nombres_apellidos_denunciante', models.CharField(max_length=255)),
                ('edad_denunciante', models.CharField(max_length=2)),
                ('correo_denunciante', models.CharField(max_length=100)),
                ('telefono_denunciante', models.CharField(max_length=13)),
                ('celular_denunciante', models.CharField(max_length=13)),
                ('direccion_denunciante', models.CharField(max_length=100)),
                ('institucion_denunciante', models.CharField(max_length=60)),
                ('cargo_denunciante', models.CharField(max_length=100)),
                ('tipo_identificacion', models.CharField(max_length=10)),
                ('indetificacion_id', models.CharField(max_length=10)),
                ('pais', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=255)),
                ('nombres_apellidos_denunciado', models.CharField(max_length=255)),
                ('institucion_denunciado', models.CharField(max_length=60)),
                ('cargo_denunciado', models.CharField(max_length=100)),
                ('parroquia_denunciado', models.CharField(max_length=30)),
                ('ciudad_denunciado', models.ForeignKey(db_column='ciudaddenunciadoid', on_delete=django.db.models.deletion.CASCADE, related_name='ciudaddenunciado', to='cpccs.Ciudad')),
                ('ciudad_denunciante', models.ForeignKey(db_column='ciudaddenuncianteid', on_delete=django.db.models.deletion.CASCADE, related_name='ciudaddenunciante', to='cpccs.Ciudad')),
                ('etnia_denunciante', models.ForeignKey(db_column='etniadenuncianteid', on_delete=django.db.models.deletion.CASCADE, related_name='etniadenunciante', to='cpccs.Etnia')),
                ('genero_denunciado', models.ForeignKey(db_column='generodenunciadoid', on_delete=django.db.models.deletion.CASCADE, related_name='generodenunciado', to='cpccs.Genero')),
                ('genero_denunciante', models.ForeignKey(db_column='generodenuncianteid', on_delete=django.db.models.deletion.CASCADE, related_name='generodenunciante', to='cpccs.Genero')),
                ('niveleducaciondenunciante', models.ForeignKey(db_column='niveleducaciondenuncianteid', on_delete=django.db.models.deletion.CASCADE, related_name='educaciondenunciante', to='cpccs.NivelEducacion')),
                ('provincia_denunciado', models.ForeignKey(db_column='provinciadenunciadoid', on_delete=django.db.models.deletion.CASCADE, related_name='provinciadenunciado', to='cpccs.Provincia')),
                ('provincia_denunciante', models.ForeignKey(db_column='provinciadenuncianteid', on_delete=django.db.models.deletion.CASCADE, related_name='provinciadenunciante', to='cpccs.Provincia')),
            ],
            options={
                'db_table': 'predenuncia ',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='tipo_requerimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'requerimiento',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'usuario',
                'ordering': ('nome',),
            },
        ),
        migrations.AddField(
            model_name='requerimiento',
            name='tipodenuncia',
            field=models.ForeignKey(db_column='tipo_requerimiento_id', on_delete=django.db.models.deletion.CASCADE, related_name='tiporequerimiento', to='cpccs.tipo_requerimiento'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='provincia',
            field=models.ForeignKey(db_column='provinciaid', on_delete=django.db.models.deletion.CASCADE, to='cpccs.Provincia'),
        ),
    ]
