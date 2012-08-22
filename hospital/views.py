# -*- coding: utf-8 -*-
from contactos.models import (Hospital, Zona)
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import (ListView, UpdateView, DetailView, CreateView,
    RedirectView, View, TemplateView)
from contactos.views import LoginRequiredView
from hospital.forms import (HospitalForm, AdministracionForm,
    CentroDeImagenesForm, HospitalizacionForm, CentroTecnicoForm, QuirofanoForm)
from hospital.models import (Administracion, CentroDeImagenes, CentroTecnico,
                             Hospitalizacion, Quirofano)

class HospitalCreateView(CreateView, LoginRequiredView):
    
    model = Hospital
    form_class = HospitalForm
    template_name = 'jqm/form.html'
    
    def get_context_data(self, **kwargs):
        
        context = super(HospitalCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Medicci - Agregar Agregar Hospital"
        return context

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
