# -*- coding: utf-8 -*-
from django import forms
from hospital.models import (Administracion, CentroDeImagenes, Hospitalizacion,
                             Quirofano)
from contactos.models import Hospital, Zona, Municipio
from contactos.widgets import JQMSelect

class HospitalForm(forms.ModelForm):
    
    class Meta:
        
        model = Hospital
    
    zona = forms.ModelChoiceField(label="",
                                  queryset=Zona.objects.all(),
                                  widget=forms.HiddenInput())
    
    municipio = forms.ModelChoiceField(queryset=Municipio.objects.all(),
                                       widget=JQMSelect())

class HospitalBaseForm(forms.ModelForm):

    hospital = forms.ModelChoiceField(label="",
                                  queryset=Hospital.objects.all(),
                                  widget=forms.HiddenInput())

class AdministracionForm(HospitalBaseForm):
    
    class Meta:
        
        model = Administracion

class CentroDeImagenesForm(HospitalBaseForm):
    
    class Meta:
        
        model = CentroDeImagenes
        exclude = ('tecnicos', 'radiologos', 'secretaria', 'jefe')

class HospitalizacionForm(HospitalBaseForm):
    
    class Meta:
        
        model = Hospitalizacion

class QuirofanoForm(HospitalBaseForm):
    
    class Meta:
        
        model = Quirofano
