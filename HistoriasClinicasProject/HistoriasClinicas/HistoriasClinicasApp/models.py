from __future__ import unicode_literals

from django.db import models


class Canton(models.Model):
    can_codigo = models.CharField(primary_key=True, max_length=10)
    pro_codigo = models.ForeignKey('Provincia', db_column='pro_codigo', blank=True, null=True)
    can_nombre = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canton'


class Contacto(models.Model):
    con_codigo = models.IntegerField(primary_key=True)
    par_codigo = models.ForeignKey('Parroquia', db_column='par_codigo', blank=True, null=True)
    con_nombre = models.CharField(max_length=60, blank=True, null=True)
    con_telefono = models.CharField(max_length=12, blank=True, null=True)
    con_trabajo = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacto'


class HistoriaClinica(models.Model):
    his_codigo = models.CharField(primary_key=True, max_length=12)
    pac_cedula = models.ForeignKey('Paciente', db_column='pac_cedula', blank=True, null=True)
    con_codigo = models.ForeignKey(Contacto, db_column='con_codigo', blank=True, null=True)
    his_fecha_creacion = models.DateField(blank=True, null=True)
    his_hora_creacion = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historia_clinica'


class Paciente(models.Model):
    pac_cedula = models.CharField(primary_key=True, max_length=10)
    tip_codigo = models.ForeignKey('TipoBeneficiario', db_column='tip_codigo', blank=True, null=True)
    can_codigo = models.ForeignKey(Canton, db_column='can_codigo', blank=True, null=True)
    par_codigo = models.ForeignKey('Parroquia', db_column='par_codigo', blank=True, null=True)
    pac_codigo = models.CharField(max_length=15, blank=True, null=True)
    pac_nombre = models.CharField(max_length=60, blank=True, null=True)
    pac_fecha_nac = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    pac_direccion = models.TextField(blank=True, null=True)
    pac_telefono = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'


class Pais(models.Model):
    pai_codigo = models.CharField(primary_key=True, max_length=5)
    pai_nombre = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pais'


class Parroquia(models.Model):
    par_codigo = models.CharField(primary_key=True, max_length=10)
    can_codigo = models.ForeignKey(Canton, db_column='can_codigo', blank=True, null=True)
    par_nombre = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parroquia'


class Provincia(models.Model):
    pro_codigo = models.CharField(primary_key=True, max_length=10)
    pai_codigo = models.ForeignKey(Pais, db_column='pai_codigo', blank=True, null=True)
    pro_nombre = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincia'


class TipoBeneficiario(models.Model):
    tip_codigo = models.CharField(primary_key=True, max_length=4)
    tip_nombre = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_beneficiario'