from django.db import models
from django.db.models.fields import DecimalField,PositiveIntegerField
from apps.configuracion.models import Raza, TipoRodeo

# Create your models here.
#Modelo para la creacion de la tabla Animal en la base de datos con los atributos descritos
#haciendo referencia a otras tablas en raza y tipo.
class Animal(models.Model):
    nombre=models.CharField(max_length=20)
    fechanacimiento=models.DateField()
    peso_inicial=DecimalField(max_digits=6,decimal_places=2)
    raza=models.ForeignKey(Raza, blank=True, null=True)
    tipo=models.ForeignKey(TipoRodeo,blank=True, null=True)
    codigo_RFID=models.CharField(max_length=10, blank=True, null=True)
    fechamuerte=models.DateField(blank=True, null=True)
    imagen_animal=models.ImageField(default="siluetavaca.png",blank=True, null=True)
    
    def __str__(self):
        return self.nombre
#Modelo para la creacion de la tabla Toro en la base de datos con los atributos descritos
class Toro(models.Model):
    nombre=models.CharField(max_length=50)
    raza=models.ForeignKey(Raza, blank=True, null=True)
    pajuelas=models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre