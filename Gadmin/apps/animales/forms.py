'''
Created on Apr 18, 2017

@author: daniel
'''
from django import forms
from .models import Animal
from apps.animales.models import Toro
from datetime import *

#formulario basado en el modelo: Animal donde se mostraran los campos descritos en fields
#mediante los widgets que se enviaran al template por medio de la clase Meta
#que contienen todos los atributos del modelo
class AnimalCrearForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields=['nombre','fechanacimiento','peso_inicial','raza','tipo','codigo_RFID','fechamuerte','imagen_animal',]
        labels= {
            'nombre':'* Nombre: ',
            'fechanacimiento':'* Fecha de nacimiento: ',
            'peso_inicial':'* Peso inicial: ',
            'raza': 'Raza: ',
            'tipo':'Tipo de Rodeo: ',
            'codigo_RFID':'Codigo RFID: ',
            'fechamuerte':'Fecha de muerte: ',
            'imagen_animal':'Imagen animal: ',
        }
        widgets={
            'nombre':forms.TextInput(attrs={ "class": "form-control","placeholder": "Ingrese nombre del animal",'required': True}),
            'fechanacimiento':forms.DateInput({'class':'input group form-control datepicker', 'placeholder':'Escoja una fecha','max':date.today()}),
            'peso_inicial':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'0000,00 kg','min':'0000.00'}),
            'raza':forms.Select(attrs={'class':'form-control', 'placeholder':'Seleccione raza'}),
            'tipo':forms.Select(attrs={'class':'form-control', 'placeholder':'Seleccione tipo'}),
            'codigo_RFID':forms.TextInput(attrs={'class':'form-control', 'required': False}),
            'fechamuerte':forms.DateInput({'class': 'form-control datepicker', 'required': False}),
            'imagen_animal':forms.FileInput(),
        }
        
class AnimalEditarForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields=['nombre','fechanacimiento','peso_inicial','raza','tipo','codigo_RFID','fechamuerte','imagen_animal',]
        labels= {
            'nombre':'* Nombre: ',
            'fechanacimiento':'* Fecha de nacimiento: ',
            'peso_inicial':'* Peso inicial: ',
            'raza': 'Raza: ',
            'tipo':'Tipo de Rodeo: ',
            'codigo_RFID':'Codigo RFID: ',
            'fechamuerte':'Fecha de muerte: ',
            'imagen_animal':'Imagen animal: ',
        }
        widgets={
            'nombre':forms.TextInput(attrs={ "class": "form-control","placeholder": "Ingrese nombre del animal",'required': True}),
            'fechanacimiento':forms.DateInput({'class':'input group form-control', 'placeholder':'Escoja una fecha','max':date.today()}),
            'peso_inicial':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'0000,00 kg','min':'0000.00'}),
            'raza':forms.Select(attrs={'class':'form-control', 'placeholder':'Seleccione raza'}),
            'tipo':forms.Select(attrs={'class':'form-control', 'placeholder':'Seleccione tipo'}),
            'codigo_RFID':forms.TextInput(attrs={'class':'form-control', 'required': False}),
            'fechamuerte':forms.DateInput({'class': 'form-control datepicker', 'required': False}),
            'imagen_animal':forms.FileInput(),
        }
#     def clean(self, *args, **kwargs):
#         peso_inicial = self.cleaned_data.get('peso_inicial', '')
#         if peso_inicial < "0,00":
#             raise forms.ValidationError("El peso debe ser mayor a cero")
#         return peso_inicial
#formulario basado en el modelo: Toro, los campos a mostrar al usuario seran los definidos en fields
#el formulario se usa en las vistas para usar al template
class ToroForm(forms.ModelForm):
    class Meta:
        model=Toro
        fields=['nombre','raza','pajuelas',]
        labels={'nombre':'Nombre del toro','raza':'Raza','pajuelas':'Numero de pajuelas',}
        widgets={'nombre':forms.TextInput(attrs={ "class": "form-control","placeholder": "Ingrese nombre del toro"}),
                 'raza':forms.Select(attrs={'class':'form-control', 'placeholder':'Seleccione raza'}),
                 'pajuelas':forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                 }