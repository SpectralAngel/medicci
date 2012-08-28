# -*- coding: utf-8 -*-
from contactos.models import (Hospital, Zona)
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import (UpdateView, DetailView, CreateView)
from contactos.views import LoginRequiredView, ContactoCreateView
from hospital.forms import (HospitalForm, AdministracionForm,
    CentroDeImagenesForm, HospitalizacionForm, CentroTecnicoForm, QuirofanoForm)
from hospital.models import (Administracion, CentroDeImagenes, Hospitalizacion,
                             Quirofano)
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

class HospitalBaseView(ContactoCreateView):
    
    def get_context_data(self, **kwargs):
        
        context = super(HospitalBaseView, self).get_context_data(**kwargs)
        context['hospital'] = self.hospital
        return context
    
    def dispatch(self, *args, **kwargs):
        
        """Obtiene la :class:`contacto` que se entrego como argumento en la
        url"""
        
        self.hospital = get_object_or_404(Hospital, pk=kwargs['hospital'])
        return super(HospitalBaseView, self).dispatch(*args, **kwargs)
    
    def get_success_url(self):
        
        return reverse('hospital', args=[self.hospital.id])

class AdministradorCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado :class:`User` que esta utilizando la aplicación
        como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.vendedores.add(self.request.user)
        self.object.administrador.add(self.hospital.administracion)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class PropietarioCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado :class:`User` que esta utilizando la aplicación
        como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.propietario.add(self.hospital.administracion)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class JefeComprasCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado :class:`User` que esta utilizando la aplicación
        como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.vendedores.add(self.request.user)
        self.object.jefe_de_compras.add(self.hospital.administracion)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class JefeQuirofanoCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado :class:`User` que esta utilizando la aplicación
        como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.vendedores.add(self.request.user)
        self.object.jefe_quirofanos.add(self.hospital.quirofano)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class InstrumentistaCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado :class:`User` que esta utilizando la aplicación
        como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.vendedores.add(self.request.user)
        self.object.instrumentista.add(self.hospital.quirofano)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class SecretariaQuirofanoCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado :class:`User` que esta utilizando la aplicación
        como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.secretaria_quirofano.add(self.hospital.quirofano)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        self.hospital.administracion.save()
        
        return HttpResponseRedirect(self.get_success_url())

class JefeTecnicoCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado :class:`User` que esta utilizando la aplicación
        como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.jefe_de_imagenes.add(self.hospital.centro_tecnico)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class SecretariaTecnicoCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado :class:`User` que esta utilizando la aplicación
        como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.vendedores.add(self.request.user)
        self.object.secretaria_imagenes.add(self.hospital.centro_tecnico)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class SocioCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado :class:`User` que esta utilizando la aplicación
        como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.hospital.administracion.socios.add(self.object)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class RadiologoCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        self.object = form.save()
        self.hospital.centro_de_imagenes.radiologos.add(self.object)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class TecnicoCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        self.object = form.save()
        self.hospital.centro_de_imagenes.tecnicos.add(self.object)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class DirectorMedicoCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        self.object = form.save()
        self.object.director_medico.add(self.hospital.hospitalizacion)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class HospitalizadorCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        self.object = form.save()
        self.object.hospitalizador.add(self.hospital.hospitalizacion)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class DoctorCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        self.object = form.save()
        self.hospital.quirofano.doctores.add(self.object)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        
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
