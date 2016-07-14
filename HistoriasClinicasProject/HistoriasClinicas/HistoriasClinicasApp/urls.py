from django.conf.urls import patterns, url

urlpatterns = patterns('HistoriasClinicasApp.views',
url(r'^$', 'index_view', name='index'),
url(r'^hisclidat', 'hisclidat', name='hisclidat'),
url(r'^bushisclidat', 'bushisclidat', name='bushisclidat'),
url(r'^template', 'template', name='template'),
url(r'^pacientedat', 'pacientedat', name='pacientedat'),
url(r'^buspacientedat', 'buspacientedat', name='buspacientedat'),
url(r'^buscontactosdat', 'buscontactosdat', name='buscontactosdat'),
url(r'^contactosdat', 'contactosdat', name='contactosdat'),
)
