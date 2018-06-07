'''
Created on 29 nov. 2017

@author: Daniel
'''
from django import forms
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm):    
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username',]
        labels={
            'first_name':'Nombre',
            'last_name':'Apellido',
            'username':'NickName',
            }
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-inline'}),
            'last_name':forms.TextInput(attrs={ "class": "form-inline"}),
            'username':forms.TextInput(attrs={'class':'form-inline'}),

        }
    
    
