from django.conf.urls import patterns, url

urlpatterns = patterns('HistoriasClinicasApp.views',
url(r'^$', 'index_view', name='index'),
)
