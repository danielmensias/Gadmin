'''
@author: Daniel
'''
from django import forms
from .models import Crecimiento, Produccion, Reproduccion, EventoSanitario
from apps.animales.models import Toro
from apps.configuracion.models import Vacuna
from random import choice
from django.contrib.admin.filters import ChoicesFieldListFilter

class CrecimientoForm(forms.ModelForm):
    class Meta:
        model = Crecimiento
        fields=['peso',]
        labels={'peso':'Peso (kg):'}
        widgets={'peso':forms.NumberInput(attrs={'class':'form-control','min':'0000.00', 'placeholder':'0000,00 Kg'}),}

class ProduccionForm(forms.ModelForm): 
    class Meta:
        model=Produccion
        fields=['volumen',] 
        labels={'volumen':'Volumen (l)'}
        widgets={'volumen':forms.NumberInput(attrs={'class':'form-control','min':'0', 'placeholder':'50 lt'}),}    
        
class InseminacionForm(forms.ModelForm):        
    class Meta:
          
        model=Reproduccion 
        fields=['fecha_reproduccion','toro',]
        widgets={'fecha_reproduccion':forms.DateInput({'class':'form-control datepicker', 'placeholder':'Escoja una fecha'}),
                 'toro':forms.Select(attrs={'class':'form-control', 'placeholder':'Seleccione toro'}),
                }

class VacunacionForm(forms.ModelForm):
    class Meta:
        model=EventoSanitario       
        fields=['fecha_evento','descripcion', 'id_tecnico']
        labels={'fecha_evento':'Fecha de vacunacion','descripcion':'Vacuna','id_tecnico':'Tecnico encargado'}
        widgets={'fecha_evento':forms.DateInput({'class':'form-control datepicker', 'placeholder':'Escoja una fecha'}),
                 'descripcion':forms.Select(attrs={'class':'form-control', 'placeholder':'Seleccione la vacuna'}),
                 'id_tecnico':forms.Select(attrs={'class':'form-control'}),
                }
        
class EventoForm(forms.ModelForm):
    class Meta:
        model=EventoSanitario  
        fields=['tipo_sanitario','descripcion','fecha_evento','id_tecnico']
        labels={'tipo_sanitario':'Tipo de Evento','id_tecnico':'Responsable'}
        widgets={'tipo_sanitario':forms.Select(attrs={'class': 'form-control','placeholder':'Seleccione un tipo de evento'}),
                 'descripcion':forms.Textarea({'class': 'form-control',"placeholder": "Ingrese la descripcion del evento"}),
                 'fecha_evento':forms.DateInput({'class':'input group form-control datepicker', 'placeholder':'Escoja una fecha'}),
                 'id_tecnico':forms.Select(attrs={'class':'form-control'}),
                }