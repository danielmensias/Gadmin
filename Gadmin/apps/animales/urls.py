from django.conf.urls import url
#importo todas las vistas de la aplicacion animales
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    #urls para acceder a los formularios crud de los animales(vacas)
    url(r'listar/$',views.AnimalesListar.as_view(), name='ani_listar'),
    url(r'crear/$',views.AnimalesCrear.as_view(), name='ani_crear'),
    url(r'editar/(?P<pk>\d+)$',views.AnimalesEditar.as_view(), name='ani_editar'),
    url(r'eliminar/(?P<pk>\d+)$',views.AnimalesBorrar.as_view(), name='ani_borrar'),  
    #urls para acceder a los formularios crud de los toros  
    url(r'crear_toro/$',views.ToroCrear.as_view(), name='toro_crear'),
    url(r'borrar_toro/(?P<pk>\d+)$',views.ToroBorrar.as_view(), name='toro_borrar'),
    url(r'editar_toro/(?P<pk>\d+)$',views.ToroEditar.as_view(), name='toro_editar'),
    url(r'listar_toro/$',views.ToroListar.as_view(), name='toro_listar'),
    
    #urls para acceder al formulario de busqueda 
    url(r'buscar/$',login_required(views.AnimalesBuscar.as_view()), name='ani_buscar'),
]