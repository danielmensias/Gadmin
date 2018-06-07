'''
Created on 23 may. 2017

@author: Daniel
'''
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    #GRUPO DE URLS PARA LAS ACCIONES POSIBLES
    #para registros de crecimiento de cada animal
    url(r'crecimiento/(?P<pk>.+)/$',login_required(views.RegistrarCrecimiento), name='ecrecimiento'),
    #para registros de produccion de cada animal
    url(r'produccion/(?P<pk>\d+)$',login_required(views.RegistrarProduccion), name='eproduccion'),
    #para el evento inseminacion
    url(r'inseminacion/(?P<pk>\d+)$',login_required(views.Inseminar), name='einseminacion'),
    #para los eventos de sanidad
    url(r'evento_sanitario/(?P<pk>\d+)$',login_required(views.Revision), name='esanitario'),
    #ver eventos asignados
    url(r'evento_asignado/(?P<pk>\d+)$',views.ListarEventosA, name='eventolistar'),
    
    
    url(r'vacunacion/(?P<pk>\d+)$',views.Vacunar, name='evacunar'),
    
    
    #GRUPO DE URL PARA ESTADISTICAS GRAFICAS
    #para mostrar la plaqueta del animal y las acciones que se pueden realizar
    url(r'varios/(?P<pk>\d+)$',login_required(views.ResumenAnimal),name='evarios'),    
    #para que se vean todos los animales que se tiene 
    url(r'estadisticas/$', views.InventarioAnimales.as_view(), name='eestadistica'),
    #para mostrar datos de la tabla produccion
    url(r'produccion/$', views.ProduccionView.as_view(), name='eproduccion'),
    #para la lista de animales con acciones de ver crecimiento y produccion
    url(r'creciyprodu/$', views.CyPAnimales.as_view(), name='cypanimales'),
    #llama al metodo que grafica el crecimiento
    url(r'crecer/(?P<pk>\d+)$',login_required(views.GraficarCrecimiento),name='anicrecer'),
    #llama al metodo que grafica la produccion
    #url(r'producir/(?P<pk>\d+)$',login_required(views.GraficarProduccion),name='aniproducir'),
    #llama al metodo que grafica los tipos de rodeos
    url(r'tipoderodeo/$',views.AnimalesTipo,name='listado'),
    
    #GRUPO DE URL PARA REPORTES
    url(r'^reporte_general/$',views.ReporteGeneral.as_view(), name='reportegen'),
    
    
    
    #revisar ya que me devuelve los valores pero no le puedo pasar al chart
    #url(r'estadisticas_ajax/$', CrecimientoAjaxView.as_view()),    
]