# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HistoriasClinicasApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='canton',
            options={'managed': False, 'verbose_name_plural': 'Lista Cantones'},
        ),
        migrations.AlterModelOptions(
            name='contacto',
            options={'managed': False, 'verbose_name_plural': 'Contactos de Emergencia'},
        ),
        migrations.AlterModelOptions(
            name='historiaclinica',
            options={'managed': False, 'verbose_name_plural': 'Historias Clinicas'},
        ),
        migrations.AlterModelOptions(
            name='paciente',
            options={'managed': False, 'verbose_name_plural': 'Lista Pacientes'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'managed': False, 'verbose_name_plural': 'Lista Paises'},
        ),
        migrations.AlterModelOptions(
            name='parroquia',
            options={'managed': False, 'verbose_name_plural': 'Lista Parroquias'},
        ),
        migrations.AlterModelOptions(
            name='provincia',
            options={'managed': False, 'verbose_name_plural': 'Lista Provincias'},
        ),
        migrations.AlterModelOptions(
            name='tipobeneficiario',
            options={'managed': False, 'verbose_name_plural': 'Tipos de Seguro'},
        ),
    ]
