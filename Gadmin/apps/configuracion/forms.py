'''
Created on Apr 19, 2017
#encoding:utf-8
@author: daniel
'''

from django import forms
from .models import Raza, TipoRodeo, Vacuna, Tecnico, TipoSanitario

#formulario de ingreso de datos para el modelo Raza
class RazaForms(forms.ModelForm):
    class Meta:
        model = Raza
        fields=['nombre',]
        labels= {'nombre':'Nombre raza',}
        widgets={'nombre':forms.TextInput(attrs={'class':'form-control', 'size':60, 'placeholder':'Ingrese el nombre de la raza'}),}
        
class TipoForms(forms.ModelForm):
    class Meta:
        model = TipoRodeo
        fields=['nombre',]
        labels= {'nombre':'Tipo de rodeo: ',}
        widgets={'nombre':forms.TextInput(attrs={'class':'form-control'}),}
        
class VacunaForms(forms.ModelForm):
    class Meta:
        model = Vacuna
        fields=['nombre',]
        labels= {'nombre':'Nombre vacuna',}
        widgets={'nombre':forms.TextInput(attrs={'class':'form-control'}),}
        
class TecnicoForm(forms.ModelForm):
    class Meta:
        model=Tecnico
        fields=['nombre_tecnico','apellido_tecnico','telefono','cedula','correo',]
        labels= {'nombre_tecnico':'Nombre','apellido_tecnico':'Apellido','telefono':'Telefono',
                 'cedula':'Cedula','correo':'Correo electronico',}
        widgets={'nombre_tecnico':forms.TextInput(attrs={'class':'form-control'}),
                 'apellido_tecnico':forms.TextInput(attrs={'class':'form-control'}),
                 'telefono':forms.NumberInput(attrs={'class':'form-control'}),
                 'cedula':forms.TextInput(attrs={'class':'form-control'}),
                 'correo':forms.EmailInput(attrs={'class':'form-control'}),}      

class SanitarioForm(forms.ModelForm):
    class Meta:
        model = TipoSanitario
        fields=['nombre',]
        labels= {'nombre':'Nombre evento sanitario',}
        widgets={'nombre':forms.TextInput(attrs={'class':'form-control'}),}
        
        
        