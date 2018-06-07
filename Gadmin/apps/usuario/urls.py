'''
Created on 29 nov. 2017

@author: Daniel
'''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'perfil/(?P<pk>\d+)$', views.PerfilUsuario.as_view(), name='perfil'),  
    url(r'notificaciones/$', views.Notificaciones, name='notificacion'),  
    
]
