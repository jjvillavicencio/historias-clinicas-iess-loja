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
url(r'^mapsprov', 'mapsprov', name='mapsprov'),
url(r'^mapscant', 'mapscant', name='mapscant'),
url(r'^perfiles/(?P<codPac>[^/]+)/$', 'perfiles', name='perfiles'),
url(r'^provinciaId/(?P<codProv>[^/]+)/$', 'provinciaId', name='provinciaId'),
url(r'^cantonId/(?P<codCanton>[^/]+)/$', 'cantonId', name='cantonId'),
)
