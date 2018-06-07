from django.db import models

# Create your models here.
#modelo para crear los tipos de razas
class Raza(models.Model):
    nombre = models.CharField(max_length=15)
    def __str__(self):
        return '{}'.format(self.nombre)
#modelo para crear el tipo de rodeo al que pertenecen los animales
class TipoRodeo(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return '{}'.format(self.nombre)
    
#modelo donde se crearan las vacunas disponibles
class Vacuna(models.Model):
    nombre=models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.nombre)
#modelo de la persona que se encargara de las revisiones   
class Tecnico(models.Model):
    nombre_tecnico=models.CharField(max_length=25)
    apellido_tecnico=models.CharField(max_length=25)
    telefono=models.CharField(max_length=10)
    cedula=models.CharField(max_length=10)
    correo=models.EmailField()
    
    def __str__(self):
        return '{}'.format(self.nombre_tecnico + " " + self.apellido_tecnico)
#modelo para definir el tipo de revisiones(registros sanitarios)
class TipoSanitario(models.Model):
    nombre=models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.nombre)
    

    