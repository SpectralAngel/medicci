# -*- coding: utf-8 -*-
from calendar import monthrange, month_name
from contactos.models import (Contacto, Especialidad, Cita, Ciclo, Departamento,
    Municipio, Direccion, Telefono, Email, Visita, Material, MaterialUtilizado,
    Cuenta)
from contactos.views import LoginRequiredView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import urlencode
from django.utils import timezone
from django.views.generic import (ListView, UpdateView, DetailView, CreateView,
    RedirectView, View, TemplateView)
from reportes.forms import ContactoSearchForm, CicloForm

class IndexView(TemplateView, LoginRequiredView):
    
    template_name = 'reportes/index.html'
    
    def get_context_data(self, **kwargs):
        
        context = super(IndexView, self).get_context_data(**kwargs)
        context['search'] = ContactoSearchForm()
        
        return context

class ContactoListView(ListView, LoginRequiredView):
    
    context_object_name = 'contactos'
    template_name = 'reportes/contactos.html'
    paginate_by = 25
    
    def get_queryset(self):
        get = self.request.GET.copy()
        if(len(get)):
            get.pop('page')
        self.baseurl = urlencode(get)
        model = Contacto
        self.form = ContactoSearchForm(self.request.GET)
        filters = model.get_queryset(self.request.GET)
        if len(filters):
            model = model.objects.filter(filters)
        else:
            model = model.objects.all()
        return model
    
    def get_context_data(self, **kwargs):
        
        context = super(ContactoListView, self).get_context_data(**kwargs)
        context['form'] = self.form
        context['baseurl']= self.baseurl
        return context

class VisitasCicloView(ListView, LoginRequiredView):
    
    context_object_name = 'visitas'
    template_name = 'reportes/visitasPeriodo.html'
    paginate_by = 25
    
    def get_queryset(self):
        
        get = self.request.GET.copy()
        
        if (len(get)):
            get.pop('page')
        
        self.form = CicloForm(self.request.GET)
        
        ciclo = self.request.GET.get('ciclo')
        self.ciclo = Ciclo.get(pk=ciclo) # @UndefinedVariable
        
        return Visita.objects.filter(
            fecha_y_hora__gte=self.ciclo.inicio,
        ).exclude(
            fecha_y_hora__gte=self.ciclo.fin,
        )
    
    def get_context_data(self, **kwargs):
        
        context = super(VisitasCicloView, self).get_context_data(**kwargs)
        context['citas'] = Cita.objects.filter(
            fecha_y_hora__gte=self.ciclo.inicio,
        ).exclude(
            fecha_y_hora__gte=self.ciclo.fin,
        ).count()
        context['contactos'] = Contacto.objects.count()
        return context

class CitasCicloView(ListView, LoginRequiredView):
    
    context_object_name = 'citas'
    template_name = 'reportes/visitasPeriodo.html'
    paginate_by = 25
    
    def get_queryset(self):
        
        get = self.request.GET.copy()
        
        if (len(get)):
            get.pop('page')
        
        self.form = CicloForm(self.request.GET)
        
        ciclo = self.request.GET.get('ciclo')
        self.ciclo = Ciclo.get(pk=ciclo) # @UndefinedVariable
        
        return Cita.objects.filter(
            fecha_y_hora__gte=self.ciclo.inicio,
        ).exclude(
            fecha_y_hora__gte=self.ciclo.fin,
        )

class VentasUsuario(ListView, LoginRequiredView):
    
    context_object_name = 'ventas'
    template_name = 'reportes/visitasPeriodo.html'
    paginate_by = 25
