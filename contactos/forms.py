# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from contactos.models import (Contacto, Especialidad, Cita, Ciclo, Departamento,
    Municipio, Direccion, Telefono, Email, Visita, Material, MaterialUtilizado,
    Cuenta)
from contactos.widgets import (DateBoxWidget, SlideTimeBoxWidget)

class ContactoForm(forms.ModelForm):
    
    class Meta:
        
        model = Contacto
        exclude = ('agregado', 'activo', )
    
    nacimiento = forms.DateField(widget=DateBoxWidget(), required=False)

class FechaHoraBaseForm(forms.ModelForm):

    fecha_y_hora = forms.DateTimeField(widget=SlideTimeBoxWidget(), required=False)

class ContactoBaseForm(forms.ModelForm):
    
    contacto = forms.ModelChoiceField(label="",
                                  queryset=Contacto.objects.all(),
                                  widget=forms.HiddenInput(), required=False)

class UsuarioBaseForm(forms.ModelForm):
    
    usuario = forms.ModelChoiceField(label="",
                                  queryset=User.objects.all(),
                                  widget=forms.HiddenInput(), required=False)

class CitaForm(ContactoBaseForm, UsuarioBaseForm, FechaHoraBaseForm):
    
    class Meta:
        
        model = Cita
        exclude = ('visitada', 'publicada',)

class VisitaForm(ContactoBaseForm, UsuarioBaseForm, FechaHoraBaseForm):
    
    class Meta:
        
        model = Visita

class TelefonoForm(ContactoBaseForm):

    class Meta:
        
        model = Telefono

class EmailForm(ContactoBaseForm):
    
    class Meta:
        
        model = Email

class DireccionForm(ContactoBaseForm):
    
    class Meta:
        
        model = Direccion

class MaterialUtilizadoForm(forms.ModelForm):
    
    class Meta:
        
        model = MaterialUtilizado
    
    visita = forms.ModelChoiceField(label="",
                                  queryset=Visita.objects.all(),
                                  widget=forms.HiddenInput(), required=False)
