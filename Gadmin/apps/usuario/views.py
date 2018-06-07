from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy
from .forms import PerfilForm
from django.views.generic.list import ListView
from apps.eventos.models import EventoSanitario
from datetime import *
class PerfilUsuario(LoginRequiredMixin,UpdateView):
    model=User
    form_class=PerfilForm
    template_name='registration/perfil_usuario.html'
    success_url=reverse_lazy('home')


def Notificaciones(request):
    inicio= datetime.now()
    dias=timedelta(days=5)
    rangodias=inicio + dias
    final=rangodias.date()
    eventosproximos=EventoSanitario.objects.filter(fecha_evento__range=[inicio,final]) 
    numeroeventos=eventosproximos.count()
    contexto={'notificaciones':eventosproximos,'contador':numeroeventos}
    return render(request,'registration/Notificaciones.html', contexto)

