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
