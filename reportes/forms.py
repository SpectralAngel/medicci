# -*- coding: utf-8 -*-
from django import forms
from contactos.models import (Contacto, Especialidad, Municipio, Cuenta, Ciclo)

class ContactoSearchForm(forms.Form):
    
    nombre = forms.CharField(max_length=100, required=False)
    apellido = forms.CharField(max_length=100, required=False)
    sexo = forms.ChoiceField(choices=Contacto.SEXOS)
    especialidades = forms.ModelMultipleChoiceField(queryset=
                                    Especialidad.objects.all(), required=False)
    ciudad = forms.ModelChoiceField(queryset=
                                    Municipio.objects.all(), required=False)
    cuentas = forms.ModelMultipleChoiceField(queryset=
                                    Cuenta.objects.all(), required=False)

class CicloForm(forms.Form):
    
    ciclo = forms.ModelChoiceField(queryset=Ciclo.objects.all())
