# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-24 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colegio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_modular', models.CharField(blank=True, max_length=15, null=True, verbose_name='Código modular')),
                ('codigo_colegio', models.CharField(blank=True, max_length=15, null=True, verbose_name='Código colegio')),
                ('anexo', models.IntegerField(default=0, null=True, verbose_name='Anexo')),
                ('codigo_local', models.CharField(blank=True, max_length=15, null=True, verbose_name='Código colegio')),
                ('forma', models.CharField(blank=True, max_length=15, null=True, verbose_name='Forma')),
                ('nivel', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nivel')),
                ('nombre', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre')),
                ('telefono', models.CharField(blank=True, max_length=50, null=True, verbose_name='Teléfono')),
                ('direccion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección')),
                ('centro_poblado', models.CharField(blank=True, max_length=100, null=True, verbose_name='Centro poblado')),
                ('ubigeo', models.CharField(blank=True, max_length=10, null=True, verbose_name='Ubigeo')),
                ('departamento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Departamento')),
                ('provincia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Provincia')),
                ('distrito', models.CharField(blank=True, max_length=100, null=True, verbose_name='Distrito')),
                ('area', models.CharField(blank=True, max_length=100, null=True, verbose_name='Área')),
                ('region', models.CharField(blank=True, max_length=100, null=True, verbose_name='Región')),
                ('ugel_codigo', models.CharField(blank=True, max_length=15, null=True, verbose_name='Ugel código')),
                ('ugel_nombre', models.CharField(blank=True, max_length=150, null=True, verbose_name='Ugel nombre')),
            ],
        ),
    ]
