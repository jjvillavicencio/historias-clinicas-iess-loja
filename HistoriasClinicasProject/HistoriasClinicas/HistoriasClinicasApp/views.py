from django.shortcuts import render, render_to_response, RequestContext
from django.core.serializers.json import json, DjangoJSONEncoder
from HistoriasClinicasApp.models import *
from django.http import HttpResponse
import datetime,json

# Create your views here.
def index_view(request):
	return render_to_response('index.html', context=RequestContext(request))
def bushisclidat(request):
	historias = HistoriaClinica.objects.all().values('his_codigo', 'pac_cedula', 'con_codigo', 'his_fecha_creacion', 'his_hora_creacion')
	return HttpResponse(json.dumps(list(historias), cls=DjangoJSONEncoder), content_type = 'application/json')
def hisclidat(request):
	return render_to_response('hisclidat.html', context=RequestContext(request))
def template(request):
	return render_to_response('template.html', context=RequestContext(request))
