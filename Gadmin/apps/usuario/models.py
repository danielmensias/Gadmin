from django.db import models
from apps.animales.models import Animal
from apps.eventos.models import Crecimiento, Produccion, EventoSanitario



# Create your models here.
class Reporte(models.Model):
    id_animal=models.ForeignKey(Animal)
    id_crecimiento=models.ForeignKey(Crecimiento)
    id_produccion=models.ForeignKey(Produccion)
    id_tratamiento=models.ForeignKey(EventoSanitario)
    

    
    