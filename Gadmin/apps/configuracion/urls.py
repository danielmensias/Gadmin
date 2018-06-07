from django.conf.urls import url

from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'general/$', TemplateView.as_view(template_name='configuracion/base_configuracion.html'), name='conf_base'),
        
    url(r'raza/listar/$', views.RazaListar.as_view(), name='raza_listar'),
    url(r'raza/crear/$', views.RazaCrear.as_view(), name='raza_crear'),
    url(r'raza/editar/(?P<pk>\d+)$', views.RazaEditar.as_view(), name='raza_editar'),
    url(r'raza/eliminar/(?P<pk>\d+)$', views.RazaBorrar.as_view(), name='raza_borrar'),
    
    url(r'tipo/crear/$', views.TipoCrear.as_view(), name='tipo_crear'),
    url(r'tipo/listar/$', views.TipoListar.as_view(), name='tipo_listar'),    
    url(r'tipo/editar/(?P<pk>\d+)$', views.TipoEditar.as_view(), name='tipo_editar'),
    url(r'tipo/eliminar/(?P<pk>\d+)$', views.TipoBorrar.as_view(), name='tipo_borrar'),
    
    url(r'vacuna/listar/$', views.VacunaListar.as_view(), name='vacu_listar'),
    url(r'vacuna/crear/$', views.VacunaCrear.as_view(), name='vacu_crear'),
    url(r'vacuna/editar/(?P<pk>\d+)$', views.VacunaEditar.as_view(), name='vacu_editar'),
    url(r'vacuna/eliminar/(?P<pk>\d+)$', views.VacunaBorrar.as_view(), name='vacu_borrar'),
    
    url(r'tecnico/crear/$', views.TecnicoCrear.as_view(), name='tec_crear'),
    url(r'tecnico/listar/$', views.TecnicoListar.as_view(), name='tec_listar'),    
    url(r'tecnico/editar/(?P<pk>\d+)$', views.TecnicoEditar.as_view(), name='tec_editar'),
    url(r'tecnico/eliminar/(?P<pk>\d+)$', views.TecnicoBorrar.as_view(), name='tec_borrar'),
    
    url(r'registro/crear/$', views.RegistroSCrear.as_view(), name='reg_crear'),
    url(r'registro/listar/$', views.RegistroSListar.as_view(), name='reg_listar'),    
    url(r'registro/editar/(?P<pk>\d+)$', views.RegistroSEditar.as_view(), name='reg_editar'),
    url(r'registro/eliminar/(?P<pk>\d+)$', views.RegistroSBorrar.as_view(), name='reg_borrar'),
]
