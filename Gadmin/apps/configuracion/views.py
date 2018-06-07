
from django.views.generic import ListView
from .models import Raza, TipoRodeo, Vacuna, Tecnico, TipoSanitario
from .forms import RazaForms, TipoForms, VacunaForms, TecnicoForm, SanitarioForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here. 
 
class RazaCrear(LoginRequiredMixin, CreateView):
    model = Raza
    form_class=RazaForms
    template_name='configuracion/config_form.html'
    success_url=reverse_lazy('configuracion:raza_listar')
    
class RazaListar(LoginRequiredMixin,ListView):
    model = Raza
    template_name='configuracion/raza_list.html'   

class RazaEditar(LoginRequiredMixin,UpdateView):
    model=Raza
    form_class=RazaForms
    template_name='configuracion/config_form.html'
    success_url=reverse_lazy('configuracion:raza_listar')

class RazaBorrar(LoginRequiredMixin,DeleteView):
    model=Raza
    template_name='configuracion/eliminar.html'
    success_url=reverse_lazy('configuracion:raza_listar')
    
class TipoListar(LoginRequiredMixin,ListView):
    model = TipoRodeo
    template_name='configuracion/rodeo_list.html'
    
class TipoCrear(LoginRequiredMixin,CreateView):
    model = TipoRodeo
    form_class=TipoForms
    template_name='configuracion/config_form.html'
    success_url=reverse_lazy('configuracion:tipo_listar')

class TipoEditar(LoginRequiredMixin,UpdateView):
    model=TipoRodeo
    form_class=TipoForms
    template_name='configuracion/config_form.html'
    success_url=reverse_lazy('configuracion:tipo_listar')

class TipoBorrar(LoginRequiredMixin,DeleteView):
    model=TipoRodeo
    template_name='configuracion/eliminar.html'  
    success_url=reverse_lazy('configuracion:tipo_listar')
    
class VacunaListar(LoginRequiredMixin,ListView):
    model = Vacuna
    template_name='configuracion/vacunas_list.html'
    
class VacunaCrear(LoginRequiredMixin,CreateView):
    model = Vacuna
    form_class=VacunaForms
    template_name='configuracion/config_form.html'
    success_url=reverse_lazy('configuracion:vacu_listar')

class VacunaEditar(LoginRequiredMixin,UpdateView):
    model=Vacuna
    form_class=VacunaForms
    template_name='configuracion/config_form.html'
    success_url=reverse_lazy('configuracion:vacu_listar')

class VacunaBorrar(LoginRequiredMixin,DeleteView):
    model=Vacuna
    template_name='configuracion/eliminar.html'
    success_url=reverse_lazy('configuracion:vacu_listar')

class TecnicoCrear(LoginRequiredMixin,CreateView):
    model=Tecnico
    form_class=TecnicoForm
    template_name='configuracion/config_form.html'
    success_url=reverse_lazy('configuracion:tec_listar')
class TecnicoListar(LoginRequiredMixin,ListView): 
    model = Tecnico
    template_name='configuracion/tecnico_list.html'
class TecnicoEditar(LoginRequiredMixin,UpdateView):
    model=Tecnico
    form_class=TecnicoForm
    template_name='configuracion/config_form.html'
    success_url=reverse_lazy('configuracion:tec_listar')
class TecnicoBorrar(LoginRequiredMixin,DeleteView):
    model=Tecnico
    template_name='configuracion/eliminartecnico.html'
    success_url=reverse_lazy('configuracion:tec_listar')

class RegistroSCrear(LoginRequiredMixin,CreateView):
    model=TipoSanitario
    form_class = SanitarioForm
    template_name='configuracion/config_form.html'
    success_url=reverse_lazy('configuracion:reg_listar')

class RegistroSListar(LoginRequiredMixin,ListView):
    model = TipoSanitario
    template_name='configuracion/evento_list.html'

class RegistroSEditar(LoginRequiredMixin,UpdateView):
    model=TipoSanitario
    form_class=SanitarioForm
    template_name='configuracion/config_form.html'
    success_url=reverse_lazy('configuracion:reg_listar')

class RegistroSBorrar(LoginRequiredMixin,DeleteView):
    model=TipoSanitario
    template_name='configuracion/eliminar.html'
    success_url=reverse_lazy('configuracion:reg_listar')


