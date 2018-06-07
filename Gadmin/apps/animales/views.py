
# Create your views here.
from django.views.generic import ListView, CreateView

from .models import Animal
from apps.animales.forms import AnimalCrearForm, ToroForm, AnimalEditarForm
from django.views.generic.edit import UpdateView, DeleteView 
from django.urls.base import reverse_lazy
from django.db.models import Q
from django.shortcuts import render_to_response
from apps.animales.models import Toro
from django.http.response import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib.messages.views import SuccessMessageMixin

#clases que manejan los eventos crud para el registro de animales
#de la hacienda, para acceder a las mismas se debe estar logeado 
#la clase LoginRequiredMixin realiza esta tarea para cada una de las vistas
class AnimalesListar(ListView):
    model = Animal
    template_name='animales/animal_list.html'
    #paginate_by=10 comentado para que funcione el datatable
    #ordering = ['id']

#clase para buscar los animales desde un listview con datatables
class AnimalesBuscar(ListView):
    model = Animal
    template_name='animales/animal_buscar.html'
        
class AnimalesCrear(LoginRequiredMixin,CreateView):
    model = Animal
    form_class=AnimalCrearForm
    template_name='animales/animal_form.html'
    success_url=reverse_lazy('animal:ani_listar')
    
  
class AnimalesEditar(LoginRequiredMixin,UpdateView):
    model=Animal
    form_class=AnimalEditarForm
    template_name='animales/animal_form.html'
    success_url=reverse_lazy('animal:ani_buscar')
    #decorador para la ejecucion de permisos del usuario
    @method_decorator(permission_required('Animal.change_animal',reverse_lazy('animal:ani_buscar')))
    def dispatch(self, *args, **kwargs):
        return super(AnimalesEditar, self).dispatch(*args, **kwargs)
    
class AnimalesBorrar(LoginRequiredMixin,DeleteView):
    model=Animal
    template_name='animales/eliminar.html'
    success_url=reverse_lazy('animal:ani_buscar')    

#clases que manejan las vistas del formulario crud de los toros 
#que se van a registrar en el sistema.
class ToroCrear(LoginRequiredMixin,CreateView):
    model=Toro
    form_class=ToroForm
    template_name='animales/toro_form.html'
    success_url=reverse_lazy('animal:toro_listar')

class ToroEditar(LoginRequiredMixin,UpdateView):
    model=Toro
    form_class=ToroForm
    template_name='animales/toro_form.html'
    success_url=reverse_lazy('animal:toro_listar')
    
class ToroListar(LoginRequiredMixin,ListView):
    model = Toro
    template_name='animales/toro_listar.html'
    paginate_by=10
    ordering = ['id']

class ToroBorrar(LoginRequiredMixin,DeleteView):
    model=Toro
    template_name='animales/eliminartoro.html'
    success_url=reverse_lazy('animal:toro_listar')

#metodo para buscar segun la coincidencia en Registro-BuscarAnimal
#dependiendo de la cadena de texto ingresada
def buscar_animal(request):    
    busqueda = request.GET.get('q', '')
    if busqueda:
        qset = (
            Q(nombre__icontains=busqueda) 
        )
        resultados = Animal.objects.filter(qset).distinct()
    else:
        resultados = []
    return render_to_response("animales/animal_buscar.html", {
        "resultados": resultados,
        "busqueda": busqueda
    })

#clase para los modales elimina el regstro pero no me permite visualizar el modal
#revisar el funconamiento una vez completado los requerimientos basicos    
def eliminar_animal(request):
    pk = request.POST.get('identificador_id')
    identificador = Animal.objects.get(pk=pk)
    identificador.delete()
    response = {}
    return JsonResponse(response)