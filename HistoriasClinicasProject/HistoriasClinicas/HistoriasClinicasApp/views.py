from django.shortcuts import render, render_to_response, RequestContext
from django.core.serializers.json import json, DjangoJSONEncoder
from HistoriasClinicasApp.models import *
from django.http import HttpResponse
import datetime,json

# Create your views here.
def index_view(request):
	return render_to_response('index.html', context=RequestContext(request))


def bushisclidat(request):
	historias = HistoriaClinica.objects.all().values(
	'his_codigo',
	'pac_cedula',
	'pac_cedula__pac_nombre',
	'con_codigo__con_nombre',
	'his_fecha_creacion',
	'his_hora_creacion',
	'pac_cedula__can_codigo__can_nombre', 'pac_cedula__can_codigo__pro_codigo__pro_nombre',
	'pac_cedula__can_codigo',
	'pac_cedula__can_codigo__pro_codigo',)

	datos_graficas = []

	for h in historias:
		obj = {}
		obj['his_codigo'] = '<a href="/perfiles/'+h['his_codigo']+'/">'+h['his_codigo']+'</a>'

		obj['pac_cedula'] = h['pac_cedula']
		obj['pac_nombre'] = h['pac_cedula__pac_nombre']
		obj['con_nombre'] = h['con_codigo__con_nombre']
		obj['his_fecha_creacion'] = h['his_fecha_creacion']
		obj['his_hora_creacion'] = h['his_hora_creacion']
		obj['pac_canton'] = '<a href="/cantonId/'+h['pac_cedula__can_codigo']+'/">'+h['pac_cedula__can_codigo__can_nombre']+'</a>'
		obj['pac_provincia'] = '<a href="/provinciaId/'+h['pac_cedula__can_codigo__pro_codigo']+'/">'+h['pac_cedula__can_codigo__pro_codigo__pro_nombre']+'</a>'

		datos_graficas.append(obj)

	return HttpResponse(json.dumps(datos_graficas, cls=DjangoJSONEncoder), content_type = 'application/json')


def hisclidat(request):

	tipos = TipoBeneficiario.objects.all().values('tip_codigo', 'tip_nombre')
	datos_tipos = [];

	for tip in tipos:
		obj = {}
		cantidad = HistoriaClinica.objects.filter(pac_cedula__tip_codigo = tip['tip_codigo']).count()
		obj['tip_codigo'] = tip['tip_codigo']
		obj['tip_nombre'] = tip['tip_nombre']
		obj['tip_cantidad'] = cantidad
		datos_tipos.append(obj)

	generos = HistoriaClinica.objects.all().values('pac_cedula__sexo').distinct()
	datos_generos = [];

	for gen in generos:
		obj = {}
		cantidad = HistoriaClinica.objects.filter(pac_cedula__sexo = gen['pac_cedula__sexo']).count()
		if gen['pac_cedula__sexo'] == 'M':
			obj['genero'] = 'Masculino'
		if gen['pac_cedula__sexo'] == 'F':
			obj['genero'] = 'Femenino'
		obj['gen_cantidad'] = cantidad
		datos_generos.append(obj)

	return render_to_response('hisclidat.html', {'datos_tipos':datos_tipos, 'datos_genero':datos_generos})


def buspacientedat(request):
	pacientes = Paciente.objects.all().values('pac_cedula', 'tip_codigo__tip_nombre', 'can_codigo__can_nombre', 'par_codigo__par_nombre', 'pac_codigo', 'pac_nombre', 'pac_fecha_nac', 'sexo', 'pac_direccion', 'pac_telefono')
	return HttpResponse(json.dumps(list(pacientes), cls=DjangoJSONEncoder), content_type = 'application/json')


def pacientedat(request):
	return render_to_response('pacientedat.html', context=RequestContext(request))


def buscontactosdat(request):
	contactos = Contacto.objects.all().values('con_codigo', 'par_codigo__par_nombre', 'con_nombre', 'con_telefono', 'con_trabajo')
	return HttpResponse(json.dumps(list(contactos), cls=DjangoJSONEncoder), content_type = 'application/json')


def contactosdat(request):
	return render_to_response('contactosdat.html', context=RequestContext(request))


def template(request):
	return render_to_response('template.html', context=RequestContext(request))


def mapsprov(request):
	lugar = Provincia.objects.all().values('pro_nombre','pro_latitud', 'pro_longitud', 'pro_codigo')

	diccionario = []
	for lugares in lugar:
		a = HistoriaClinica.objects.filter(pac_cedula__par_codigo__can_codigo__pro_codigo = lugares['pro_codigo'])

		diccionario.append(
		{'provincia':lugares['pro_nombre'],
		'cantidad':len(a),
		'latitud':lugares['pro_latitud'],
		'longitud':lugares['pro_longitud'],
		'codigo':lugares['pro_codigo'],
		'porcentaje':(len(a)*100)/16771})

	return render(request, 'mapsprov.html', {'lugar':lugar, 'diccionario':diccionario})


def mapscant(request):
	lugar = Canton.objects.all().values('can_codigo','pro_codigo', 'can_nombre', 'latitud', 'longitud')
	diccionario = []

	for lugares in lugar:
		a = HistoriaClinica.objects.filter(pac_cedula__par_codigo__can_codigo = lugares['can_codigo'])

		diccionario.append({
		'canton':lugares['can_nombre'],
		'cantidad':len(a),
		'latitud':lugares['latitud'],
		'longitud':lugares['longitud'],
		'codigo':lugares['can_codigo'],
		'porcentaje':(len(a)*100)/16771})

	return render(request, 'mapscant.html', {'lugar':lugar, 'diccionario':diccionario})


def perfiles(request, codPac=None):
	perfil = HistoriaClinica.objects.filter(his_codigo = codPac).values('pac_cedula__pac_nombre', 'his_codigo', 'pac_cedula', 'pac_cedula__pac_fecha_nac', 'pac_cedula__sexo', 'pac_cedula__pac_direccion', 'pac_cedula__pac_telefono', 'his_fecha_creacion', 'his_hora_creacion', 'con_codigo__con_nombre', 'con_codigo__con_telefono', 'pac_cedula__can_codigo__can_nombre', 'pac_cedula__can_codigo__pro_codigo__pro_nombre', 'pac_cedula__can_codigo', 'pac_cedula__can_codigo__pro_codigo')

	return render(request, 'perfiles.html', {'perfil':perfil})


def provinciaId(request, codProv=None):
	tipos = TipoBeneficiario.objects.all().values('tip_codigo', 'tip_nombre')
	nombre = Provincia.objects.filter(pro_codigo = codProv).values('pro_nombre')
	datos_tipos = [];

	for tip in tipos:
		obj = {}
		cantidad = HistoriaClinica.objects.filter(pac_cedula__tip_codigo = tip['tip_codigo'], pac_cedula__can_codigo__pro_codigo = codProv).count()
		obj['tip_codigo'] = tip['tip_codigo']
		obj['tip_nombre'] = tip['tip_nombre']
		obj['tip_cantidad'] = cantidad
		datos_tipos.append(obj)

	a = nombre[0]['pro_nombre']

	generos = HistoriaClinica.objects.all().values('pac_cedula__sexo').distinct()
	datos_generos = [];

	for gen in generos:
		obj = {}
		cantidad = HistoriaClinica.objects.filter(pac_cedula__sexo = gen['pac_cedula__sexo'], pac_cedula__can_codigo__pro_codigo__pro_nombre = a).count()
		if gen['pac_cedula__sexo'] == 'M':
			obj['genero'] = 'Masculino'
		if gen['pac_cedula__sexo'] == 'F':
			obj['genero'] = 'Femenino'
		obj['gen_cantidad'] = cantidad
		datos_generos.append(obj)

	return render(request, 'provinciaid.html', {'datos_tipos':datos_tipos, 'provincia':a, 'gener_dat':datos_generos})


def cantonId(request, codCanton=None):
	tipos = TipoBeneficiario.objects.all().values('tip_codigo', 'tip_nombre')
	nombre = Canton.objects.filter(can_codigo = codCanton).values('can_nombre')
	datos_tipos = [];

	for tip in tipos:
		obj = {}
		cantidad = HistoriaClinica.objects.filter(pac_cedula__tip_codigo = tip['tip_codigo'], pac_cedula__can_codigo = codCanton).count()
		obj['tip_codigo'] = tip['tip_codigo']
		obj['tip_nombre'] = tip['tip_nombre']
		obj['tip_cantidad'] = cantidad
		datos_tipos.append(obj)

	a = nombre[0]['can_nombre']

	generos = HistoriaClinica.objects.all().values('pac_cedula__sexo').distinct()
	datos_generos = [];

	for gen in generos:
		obj = {}
		cantidad = HistoriaClinica.objects.filter(pac_cedula__sexo = gen['pac_cedula__sexo'], pac_cedula__can_codigo__can_nombre = a).count()
		if gen['pac_cedula__sexo'] == 'M':
			obj['genero'] = 'Masculino'
		if gen['pac_cedula__sexo'] == 'F':
			obj['genero'] = 'Femenino'
		obj['gen_cantidad'] = cantidad
		datos_generos.append(obj)

	return render(request, 'cantonid.html', {'datos_tipos':datos_tipos, 'canton':a, 'gener_dat':datos_generos})
