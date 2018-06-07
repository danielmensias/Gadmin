from django.shortcuts import render, redirect
from .forms import CrecimientoForm, ProduccionForm, InseminacionForm, VacunacionForm
from apps.animales.models import Animal, Toro
from django.views.generic.list import ListView
from .models import Crecimiento, Produccion
from django.views.generic.base import View
from django.http.response import HttpResponse
from apps.eventos.forms import EventoForm
#librerias para la ejecucion de reporteris en la aplicacion
from Gadmin.settings import MEDIA_ROOT
from _io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus.tables import TableStyle, Table
from apps.configuracion.models import Raza, TipoRodeo
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.eventos.models import EventoSanitario
from django.db.models.aggregates import Avg, Max, Min
from django.views.generic.edit import DeleteView
from django.urls.base import reverse_lazy


# En este apartado se crean las vistas para la aplicacion eventos las cuales estan basadas en clases o en funciones 
#dependiendo de la necesidad que se tenga en cada una de ellas.
def ResumenDatos(request):
    totalanimales=Animal.objects.count()
    context = {'todos':totalanimales}
    print(context)
    return render(request, 'base/home.html', context) 


#vista basada en clase para mostrar los animales y su peso inicial en el grafico que se genera en el 
#template estadisticas.html
class InventarioAnimales(LoginRequiredMixin,ListView):
    model=Animal   
    template_name='eventos/inventario.html'
    context_object_name='animales'

#vista para mostrar la produccion en tabla(de todos los animales), en el grafico del template produccion.html    
class ProduccionView(LoginRequiredMixin,ListView):
    model=Produccion   
    template_name='eventos/produccion.html'
    context_object_name='prod'

#metodo para obtener los pesos y la fecha de las medidas de produccion de cada animal
#(aun no esta bien implementado) solo me devuelve los valores dependiendo del select del combobox   
# class CrecimientoAjaxView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         id_ani=request.GET['id']
#         medidas=Crecimiento.objects.filter(id_animal__id=id_ani)
#         data=serializers.serialize('json',medidas,fields=('peso','fecha_medida'))
#         print(data)
#         return HttpResponse(data, content_type='application/json')

#funcion que me permite almacenar el peso de cada animal por su id
def RegistrarCrecimiento(request, pk):
    if request.method == 'POST':        
        crecimiento = CrecimientoForm(request.POST)
        if crecimiento.is_valid(): 
            crecer=crecimiento.save(commit=False)
            crecer.id_animal=Animal.objects.get(id=pk)
            #crecer.id_animal=pk #me pide que sea uns instancia de animal
            crecer.save()
        return redirect('animal:ani_listar')
    else:
        crecimiento = CrecimientoForm()
    
    return render(request, 'eventos/registro_form.html', {'form':crecimiento})

#funcion que me pemrite almacenar la produccion(volumen) de cada animal por su id
def RegistrarProduccion(request, pk):
    if request.method == 'POST':        
        form = ProduccionForm(request.POST)
        if form.is_valid(): 
            produ=form.save(commit=False)
            produ.id_animal=Animal.objects.get(id=pk)
            produ.save()
        return redirect('animal:ani_listar')
    else:
        form = ProduccionForm()
        
    return render(request, 'eventos/registro_form.html', {'form':form})

#metodo para devolver los datos del animal y las acciones que se pueden realizar en un
#mismo form
def ResumenAnimal(request,pk):
    animal = Animal.objects.get(id=pk)
    context = {'ani': animal}
    return render(request, 'eventos/eventosbase.html', context)

#funcion que me permite almacenar las inseminaciones de cada animal por su id desde el boton eventos-varios
#donde sale una plaqueta con las caracteristicas del animal y los eventos 
#que se pueden realizar en el mismo
def Inseminar(request, pk):
    if request.method == 'POST':        
        form = InseminacionForm(request.POST)
        
        if form.is_valid(): 
            produ=form.save(commit=False)            
            produ.id_animal=Animal.objects.get(id=pk)            
            produ.save()
                        
        return redirect('animal:ani_listar')
    else:
        form = InseminacionForm()
        
    return render(request, 'eventos/registrainseminacion.html', {'form':form})

def Vacunar(request, pk):
    if request.method == 'POST':        
        form = VacunacionForm(request.POST)
        if form.is_valid(): 
            vacu=form.save(commit=False)
            vacu.id_animal=Animal.objects.get(id=pk)  
            vacu.tipo_sanitario=2     
            vacu.save()
        return redirect('animal:ani_listar')
    else:
        form = VacunacionForm()
        
    return render(request, 'eventos/registravacunacion.html', {'form':form})

def Revision(request, pk):
    if request.method == 'POST':        
        form = EventoForm(request.POST)
        if form.is_valid(): 
            evento=form.save(commit=False)
            evento.id_animal=Animal.objects.get(id=pk)
            evento.save()
        return redirect('animal:ani_listar')        
        
    else:
        form = EventoForm()        
    return render(request, 'eventos/registro_form.html',
                   {'form':form})
    
#clase que realiza el reporte en formato pdf de las configuraciones y datos generales que contiene la 
#aplicacion como listado de animales, razas, tecnicos, toros.
class ReporteGeneral(LoginRequiredMixin,View):
        def cabecera(self,pdf):
            #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
            archivo_imagen = MEDIA_ROOT+'/icono.png'
            #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
            pdf.drawImage(archivo_imagen, 40, 740, 100, 90,preserveAspectRatio=True)
            #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
            pdf.setFont("Helvetica", 16)
            #Dibujamos una cadena en la ubicación X,Y especificada
            pdf.drawCentredString(350, 790, u"SOFTWARE PARA LA ADMINISTRACION DE GANADO")
            pdf.setFont("Helvetica", 14)
            pdf.drawString(250, 770, u"REPORTE GENERAL")        
                        
        def tabla(self,pdf):                        
            #Se crea una lista de tuplas que van a contener los datos de todos los animales           
            encabezados = ('Nombre', 'Fecha nacimiento', 'Raza', 'Tipo de Rodeo')
            parametros = [(p.nombre, p.fechanacimiento, p.raza, p.tipo) for p in Animal.objects.all()]
                    
            t = Table([encabezados] + parametros)
            t.setStyle(TableStyle(
                [
                    ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
                    ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
                    ('BACKGROUND', (0, 0), (-1, 0), colors.green)
                ]
            ))
            #Establecemos el tamaño de la hoja que ocupará la tabla
            t.wrapOn(pdf, 50, 80) 
            #Definimos la coordenada donde se dibujará la tabla
            t.drawOn(pdf, 140,280)
            
        
        def razas(self,pdf):
            #Se crea una lista de tuplas que van a contener los datos de todos los animales           
            encabezados = ('Codigo', 'Nombre')
            parametros = [(p.id, p.nombre) for p in Raza.objects.all()]
                    
            t = Table([encabezados] + parametros)
            t.setStyle(TableStyle(
                [
                    ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
                    ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
                    ('BACKGROUND', (0, 0), (-1, 0), colors.green)
                ]
            ))
            
            #Establecemos el tamaño de la hoja que ocupará la tabla
            t.wrapOn(pdf, 640, 480) 
            #Definimos la coordenada donde se dibujará la tabla
            t.drawOn(pdf, 200,200)
            
        def get(self, request, *args, **kwargs):
            #Indicamos el tipo de contenido a devolver, en este caso un pdf
            response = HttpResponse(content_type='application/pdf')
            #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
            buffer = BytesIO()
            #Canvas nos permite hacer el reporte con coordenadas X y Y
            pdf = canvas.Canvas(buffer)
            #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
            self.cabecera(pdf)
            self.tabla(pdf)
            self.razas(pdf)
            #Con show page hacemos un corte de página para pasar a la siguiente
            pdf.showPage()
            pdf.save()
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response
    
#Vista que me muestra la lista de animales con las opciones de ver el
#crecimeinto y la produccion de cada uno de ellos.
class CyPAnimales(LoginRequiredMixin,ListView):
    model = Animal
    template_name='eventos/crec_prod_animales.html'
    paginate_by=10
    ordering = ['id']

#metodo para graficar el crecimiento y la produccion del animal desde su peso inicial
def GraficarCrecimiento(request,pk):
    pesoinicial=Animal.objects.get(id=pk)
    pesos = Crecimiento.objects.filter(id_animal__id=pk)
    medidas=Produccion.objects.filter(id_animal__id=pk)
    
    avgpeso=Crecimiento.objects.filter(id_animal__id=pk).aggregate(Promedio=Avg('peso'),Maximo= Max('peso'),Minimo= Min('peso'))
    avgproduccion=Produccion.objects.filter(id_animal__id=pk).aggregate(Promedio=Avg('volumen'),Maximo= Max('volumen'),Minimo= Min('volumen'))
    
    context = {'pesoinicial':pesoinicial, 'peso': pesos,'volumenes':medidas,'avgpeso':avgpeso,'avgproduccion':avgproduccion,}
    print(context)
    return render(request, 'eventos/graf_crecimiento.html', context) 
#metodo para graficar la produccion del animal
# def GraficarProduccion(request,pk):
#     medidas=Produccion.objects.filter(id_animal__id=pk)
#     context={'volumenes':medidas}
#     return render(request,'eventos/graf_produccion.html',context)


#Lista animales por tipo y muestra en el grafico del template
    
def AnimalesTipo(request):
    tiposrodeo=TipoRodeo.objects.all()
    nombres=[]
    arreglo=[]
    for rodeo in tiposrodeo:
        numeroanimal = Animal.objects.filter(tipo_id=rodeo.id)        
        contador=numeroanimal.count()
        nombres.append(rodeo.nombre)
        arreglo.append(contador)       

    contexto={'tiporodeo':nombres,'cantidad':arreglo}    
    return render(request,'eventos/tiporodeo.html', contexto)

# def ConfirmarEvento(request,pk,nombre):
#     envio_evento=Eventos.objects.get(pk=pk)
#     encargado= User.objects.get(username=nombre)
#     lista_suscriptor=Suscriptores.objects.all()
#     for suscriptor in lista_suscriptor:
#         reporte=ReportesEventos(id_suscriptor=suscriptor,
#                                 evento=envio_evento,
#                                 admin_user=encargado) 
#         reporte.save()   
#     return render(request, 'confirmar_evento.html')
        
#class ListarEventosA(LoginRequiredMixin,ListView):
#    model=EventoSanitario
#    template_name="eventos/eventosasignados.html"       
    
def ListarEventosA(request,pk):
    eventosani=EventoSanitario.objects.filter(id_animal_id=pk)    
    context = {'eventos':eventosani}
    print(context)  
    return render(request, 'eventos/eventosasignados.html', context) 
    

    
