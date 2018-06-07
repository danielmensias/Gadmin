from django.db import models
from django.db.models.fields.related import ForeignKey
from apps.animales.models import Animal, Toro
from apps.configuracion.models import Tecnico,TipoSanitario

# Create your models here.
class EventoSanitario(models.Model):
    tipo_sanitario=ForeignKey(TipoSanitario)
    descripcion=models.TextField(null= True)
    fecha_evento=models.DateTimeField()
    id_animal=models.ForeignKey(Animal)
    id_tecnico=models.ForeignKey(Tecnico)
        
class Produccion(models.Model):
    volumen= models.DecimalField(max_digits=4,decimal_places=2)
    id_animal=models.ForeignKey(Animal) 
    fecha_produccion=models.DateField(auto_now_add=True)
    
class Crecimiento(models.Model):
    id_animal=models.ForeignKey(Animal)
    peso=models.DecimalField(max_digits=4,decimal_places=2)
    fecha_medida=models.DateField(auto_now_add=True)     
   
class Reproduccion(models.Model):
    fecha_reproduccion=models.DateField(null=True)
    toro=models.ForeignKey(Toro)
    id_animal=models.ForeignKey(Animal)
    
    
    