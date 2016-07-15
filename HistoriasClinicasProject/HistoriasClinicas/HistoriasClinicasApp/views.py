from django.shortcuts import render, render_to_response, RequestContext
from django.core.serializers.json import json, DjangoJSONEncoder
from HistoriasClinicasApp.models import *
from django.http import HttpResponse
import datetime,json

# Create your views here.
def index_view(request):
	return render_to_response('index.html', context=RequestContext(request))
def bushisclidat(request):
	historias = HistoriaClinica.objects.all().values('his_codigo', 'pac_cedula', 'pac_cedula__pac_nombre', 'con_codigo__con_nombre', 'his_fecha_creacion', 'his_hora_creacion')
	return HttpResponse(json.dumps(list(historias), cls=DjangoJSONEncoder), content_type = 'application/json')
def hisclidat(request):
	return render_to_response('hisclidat.html', context=RequestContext(request))
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
		diccionario.append({'provincia':lugares['pro_nombre'],'cantidad':len(a), 'latitud':lugares['pro_latitud'], 'longitud':lugares['pro_longitud'], 'porcentaje':(len(a)*100)/16771})
	return render(request, 'mapsprov.html', {'lugar':lugar, 'diccionario':diccionario})
def mapscant(request):
	lugar = Canton.objects.all().values('can_codigo','pro_codigo', 'can_nombre', 'latitud', 'longitud')
	diccionario = []
	for lugares in lugar:
		a = HistoriaClinica.objects.filter(pac_cedula__par_codigo__can_codigo = lugares['can_codigo'])
		diccionario.append({'canton':lugares['can_nombre'],'cantidad':len(a), 'latitud':lugares['latitud'], 'longitud':lugares['longitud'], 'porcentaje':(len(a)*100)/16771})
	return render(request, 'mapscant.html', {'lugar':lugar, 'diccionario':diccionario})
