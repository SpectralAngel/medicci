# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from contactos.models import (Contacto, Especialidad, Cita, Ciclo, Departamento,
    Municipio, Direccion, Telefono, Email, Visita, Material, MaterialUtilizado,
    Cuenta, Asociacion, Profile, Zona, Hospital)
from contactos.widgets import (DateBoxWidget, SlideTimeBoxWidget,
                               JQMSelectMultiple, JQMSelect, SlideBoxWidget)

class ContactoForm(forms.ModelForm):
    
    class Meta:
        
        model = Contacto
        exclude = ('agregado', 'activo', )
    
    nacimiento = forms.DateField(widget=DateBoxWidget(), required=False)
    especialidades = forms.ModelMultipleChoiceField(
                                  queryset=Especialidad.objects.all(),
                                  widget=JQMSelectMultiple())
    vendedores = forms.ModelMultipleChoiceField(
                                  queryset=User.objects.all(),
                                  widget=JQMSelectMultiple())
    hospitales = forms.ModelMultipleChoiceField(
                                  queryset=Hospital.objects.all(),
                                  widget=JQMSelectMultiple())
    asociaciones = forms.ModelMultipleChoiceField(
                                  queryset=Asociacion.objects.all(),
                                  widget=JQMSelectMultiple())

class FechaHoraBaseForm(forms.ModelForm):

    fecha_y_hora = forms.DateTimeField(widget=SlideTimeBoxWidget(), required=False)

class FinalForm(forms.ModelForm):
    
    fin = forms.DateTimeField(widget=SlideTimeBoxWidget(), required=False)

class ContactoBaseForm(forms.ModelForm):
    
    contacto = forms.ModelChoiceField(label="",
                                  queryset=Contacto.objects.all(),
                                  widget=forms.HiddenInput(), required=False)

class UsuarioBaseForm(forms.ModelForm):
    
    usuario = forms.ModelChoiceField(label="",
                                  queryset=User.objects.all(),
                                  widget=forms.HiddenInput(), required=False)

class CitaForm(ContactoBaseForm, UsuarioBaseForm, FechaHoraBaseForm, FinalForm):
    
    class Meta:
        
        model = Cita
        exclude = ('visitada', 'publicada',)

class VisitaForm(ContactoBaseForm, UsuarioBaseForm, FechaHoraBaseForm,
                 FinalForm):
    
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

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        
        # magic 
        self.user = kwargs['instance'].user
        user_kwargs = kwargs.copy()
        user_kwargs['instance'] = self.user
        self.uf = UserForm(*args, **user_kwargs)
        # magic end 
        
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        self.fields.update(self.uf.fields)
        self.initial.update(self.uf.initial)
    
    def save(self, *args, **kwargs):
        # save both forms
        self.uf.save(*args, **kwargs)
        return super(ProfileForm, self).save(*args, **kwargs)
    
    class Meta:
        
        model = Profile
        exclude = ('user', 'configurado',)
    
    fecha_de_nacimiento = forms.DateField(widget=SlideBoxWidget())
    zona = forms.ModelChoiceField(label="",
                                  queryset=Zona.objects.all(),
                                  widget=JQMSelect(), required=False)
