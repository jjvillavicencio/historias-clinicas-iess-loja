# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canton',
            fields=[
                ('can_codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('can_nombre', models.CharField(max_length=60, null=True, blank=True)),
            ],
            options={
                'db_table': 'canton',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('con_codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('con_nombre', models.CharField(max_length=60, null=True, blank=True)),
                ('con_telefono', models.CharField(max_length=12, null=True, blank=True)),
                ('con_trabajo', models.CharField(max_length=60, null=True, blank=True)),
            ],
            options={
                'db_table': 'contacto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('his_codigo', models.CharField(max_length=12, serialize=False, primary_key=True)),
                ('his_fecha_creacion', models.DateField(null=True, blank=True)),
                ('his_hora_creacion', models.TimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'historia_clinica',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('pac_cedula', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('pac_codigo', models.CharField(max_length=15, null=True, blank=True)),
                ('pac_nombre', models.CharField(max_length=60, null=True, blank=True)),
                ('pac_fecha_nac', models.DateField(null=True, blank=True)),
                ('sexo', models.CharField(max_length=1, null=True, blank=True)),
                ('pac_direccion', models.TextField(null=True, blank=True)),
                ('pac_telefono', models.CharField(max_length=12, null=True, blank=True)),
            ],
            options={
                'db_table': 'paciente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('pai_codigo', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('pai_nombre', models.CharField(max_length=60, null=True, blank=True)),
            ],
            options={
                'db_table': 'pais',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('par_codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('par_nombre', models.CharField(max_length=60, null=True, blank=True)),
            ],
            options={
                'db_table': 'parroquia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('pro_codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('pro_nombre', models.CharField(max_length=60, null=True, blank=True)),
            ],
            options={
                'db_table': 'provincia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoBeneficiario',
            fields=[
                ('tip_codigo', models.CharField(max_length=4, serialize=False, primary_key=True)),
                ('tip_nombre', models.CharField(max_length=60, null=True, blank=True)),
            ],
            options={
                'db_table': 'tipo_beneficiario',
                'managed': False,
            },
        ),
    ]
