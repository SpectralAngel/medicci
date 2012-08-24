# -*- coding: utf-8 -*-
from contactos.models import (Hospital, Zona)
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import (ListView, UpdateView, DetailView, CreateView,
    RedirectView, View, TemplateView)
from contactos.views import LoginRequiredView, ContactoCreateView
from hospital.forms import (HospitalForm, AdministracionForm,
    CentroDeImagenesForm, HospitalizacionForm, CentroTecnicoForm, QuirofanoForm)
from hospital.models import (Administracion, CentroDeImagenes, CentroTecnico,
                             Hospitalizacion, Quirofano)
from django.http import HttpResponseRedirect

class HospitalCreateView(CreateView, LoginRequiredView):
    
    model = Hospital
    form_class = HospitalForm
    template_name = 'jqm/form.html'
    
    def get_context_data(self, **kwargs):
        
        context = super(HospitalCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Medicci - Agregar Hospital"
        context['zona'] = self.zona
        return context
    
    def get_form_kwargs(self):
        
        """Agrega la :class:`contacto` obtenida como el valor a utilizar en el
        formulario que será llenado posteriormente"""

        kwargs = super(HospitalCreateView, self).get_form_kwargs()
        kwargs.update({'initial':{'zona':self.zona.id}})
        return kwargs
    
    def dispatch(self, *args, **kwargs):
        
        """Obtiene la :class:`contacto` que se entrego como argumento en la
        url"""

        self.zona = get_object_or_404(Zona, pk=kwargs['zona'])
        return super(HospitalCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        
        """Guarda el objeto generado espeficando la :class:`contacto` obtenida
        de los argumentos y el :class:`User` que esta utilizando la aplicación
        """

        self.object = form.save(commit=False)
        self.object.zona = self.zona
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

def HospitalBaseView(View):
    
    def get_context_data(self, **kwargs):
        
        context = super(HospitalBaseView, self).get_context_data(**kwargs)
        context['hospital'] = self.hospital
        return context
    
    def dispatch(self, *args, **kwargs):
        
        """Obtiene la :class:`contacto` que se entrego como argumento en la
        url"""

        self.hospital = get_object_or_404(Hospital, pk=kwargs['hospital'])
        return super(HospitalBaseView, self).dispatch(*args, **kwargs)

class AdministradorCreateView(ContactoCreateView, HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado :class:`User` que esta utilizando la aplicación
        como vendedor asignado a este contacto
        """
        
        self.object = form.save(commit=False)
        self.hospital.administracion.administrador = self.object
        self.object.vendedores.add(self.request.user)
        self.object.save()
        self.hospital.administracion.save()
        
        return HttpResponseRedirect(self.get_success_url())

class PropietarioCreateView(ContactoCreateView, HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado :class:`User` que esta utilizando la aplicación
        como vendedor asignado a este contacto
        """
        
        self.object = form.save(commit=False)
        self.hospital.administracion.propietario = self.object
        self.object.vendedores.add(self.request.user)
        self.object.save()
        self.hospital.administracion.save()
        
        return HttpResponseRedirect(self.get_success_url())

class JefeComprasCreateView(ContactoCreateView, HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado :class:`User` que esta utilizando la aplicación
        como vendedor asignado a este contacto
        """
        
        self.object = form.save(commit=False)
        self.hospital.administracion.jefe_de_compras = self.object
        self.object.vendedores.add(self.request.user)
        self.object.save()
        self.hospital.administracion.save()
        
        return HttpResponseRedirect(self.get_success_url())

class JefeQuirofanoCreateView(ContactoCreateView, HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado :class:`User` que esta utilizando la aplicación
        como vendedor asignado a este contacto
        """
        
        self.object = form.save(commit=False)
        self.hospital.quirofano.jefe = self.object
        self.object.vendedores.add(self.request.user)
        self.object.save()
        self.hospital.administracion.save()
        
        return HttpResponseRedirect(self.get_success_url())

class InstrumentistaCreateView(ContactoCreateView, HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado :class:`User` que esta utilizando la aplicación
        como vendedor asignado a este contacto
        """
        
        self.object = form.save(commit=False)
        self.hospital.quirofano.instrumentista = self.object
        self.object.vendedores.add(self.request.user)
        self.object.save()
        self.hospital.administracion.save()
        
        return HttpResponseRedirect(self.get_success_url())

class SecretariaQuirofanoCreateView(ContactoCreateView, HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado :class:`User` que esta utilizando la aplicación
        como vendedor asignado a este contacto
        """
        
        self.object = form.save(commit=False)
        self.hospital.quirofano.secretaria = self.object
        self.object.vendedores.add(self.request.user)
        self.object.save()
        self.hospital.administracion.save()
        
        return HttpResponseRedirect(self.get_success_url())

class JefeTecnicoCreateView(ContactoCreateView, HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado :class:`User` que esta utilizando la aplicación
        como vendedor asignado a este contacto
        """
        
        self.object = form.save(commit=False)
        self.hospital.centro_tecnico.jefe = self.object
        self.object.vendedores.add(self.request.user)
        self.object.save()
        self.hospital.administracion.save()
        
        return HttpResponseRedirect(self.get_success_url())

class SecretariaTecnicoCreateView(ContactoCreateView, HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado :class:`User` que esta utilizando la aplicación
        como vendedor asignado a este contacto
        """
        
        self.object = form.save(commit=False)
        self.hospital.centro_tecnico.secretaria = self.object
        self.object.vendedores.add(self.request.user)
        self.object.save()
        self.hospital.administracion.save()
        
        return HttpResponseRedirect(self.get_success_url())

class HospitalUpdateView(UpdateView, LoginRequiredView):
    
    model = Hospital
    form_class = HospitalForm
    template_name = 'jqm/form.html'
    
    def get_context_data(self, **kwargs):
        
        context = super(HospitalCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Medicci - Actualizar {0}".format(self.object)
        return context

class HospitalDetailView(DetailView, LoginRequiredView):
    
    model = Hospital
    context_object_name = 'hospital'

class AdministracionUpdateView(UpdateView, LoginRequiredView):
    
    model = Administracion
    form_class = AdministracionForm
    template_name = 'jqm/form.html'

class CentroDeImagenesUpdateView(UpdateView, LoginRequiredView):
    
    model = CentroDeImagenes
    form_class = CentroDeImagenesForm
    template_name = 'jqm/form.html'

class HospitalizacionUpdateView(UpdateView, LoginRequiredView):
    
    model = Hospitalizacion
    form_class = HospitalizacionForm
    template_name = 'jqm/form.html'

class QuirofanoUpdateView(UpdateView, LoginRequiredView):
    
    model = Quirofano
    form_class = QuirofanoForm
    template_name = 'jqm/form.html'

class CentroTecnicoUpdateView(UpdateView, LoginRequiredView):
    
    model = CentroTecnico
    form_class = CentroTecnicoForm
    template_name = 'jqm/form.html'
