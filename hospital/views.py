# -*- coding: utf-8 -*-
from contactos.models import (Hospital, Zona)
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import (UpdateView, DetailView, CreateView,
                                  RedirectView)
from contactos.views import LoginRequiredView, ContactoCreateView
from hospital.forms import (HospitalForm, AdministracionForm, QuirofanoForm,
    CentroDeImagenesForm, HospitalizacionForm)
from hospital.models import (Administracion, CentroDeImagenes, Hospitalizacion,
                             Quirofano, Tomografia, ResonanciaMagenetica,
    Densitometria, Fluoroscopia, Ecografia, Mamografia, Consultorio)
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
        
        """Guarda el objeto generado colocando el :class:`User` que esta
        utilizando la aplicación como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.vendedores.add(self.request.user)
        self.object.administrador.add(self.hospital.administracion)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class PropietarioCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado colocando el :class:`User` que esta
        utilizando la aplicación como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.propietario.add(self.hospital.administracion)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class JefeComprasCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado colocando el :class:`User` que esta
        utilizando la aplicación como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.vendedores.add(self.request.user)
        self.object.jefe_de_compras.add(self.hospital.administracion)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class JefeQuirofanoCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado colocando el :class:`User` que esta
        utilizando la aplicación como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.vendedores.add(self.request.user)
        self.object.jefe_quirofanos.add(self.hospital.quirofano)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class InstrumentistaCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado colocando el :class:`User` que esta
        utilizando la aplicación como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.vendedores.add(self.request.user)
        self.object.instrumentistas.add(self.hospital.quirofano)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class AnestesiologoCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado colocando el :class:`User` que esta
        utilizando la aplicación como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.vendedores.add(self.request.user)
        self.object.instrumentistas.add(self.hospital.quirofano)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class SecretariaQuirofanoCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado colocando el :class:`User` que esta
        utilizando la aplicación como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.secretaria_quirofano.add(self.hospital.quirofano)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        self.hospital.administracion.save()
        
        return HttpResponseRedirect(self.get_success_url())

class LicenciadoQuirofanoCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado colocando el :class:`User` que esta
        utilizando la aplicación como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.licenciado_quirofano.add(self.hospital.quirofano)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        self.hospital.administracion.save()
        
        return HttpResponseRedirect(self.get_success_url())

class JefeImagenesCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado colocando el :class:`User` que esta
        utilizando la aplicación como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.jefe_de_imagenes.add(self.hospital.centro_tecnico)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class SecretariaImagenesCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado colocando el :class:`User` que esta
        utilizando la aplicación como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.vendedores.add(self.request.user)
        self.object.secretaria_imagenes.add(self.hospital.centro_tecnico)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class SocioCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado colocando el :class:`User` que esta
        utilizando la aplicación como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.hospital.administracion.socios.add(self.object)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class RadiologoCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado colocando el :class:`User` que esta
        utilizando la aplicación como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.hospital.centro_de_imagenes.radiologos.add(self.object)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class TecnicoCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado colocando el :class:`User` que esta
        utilizando la aplicación como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.hospital.centro_de_imagenes.tecnicos.add(self.object)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class DirectorMedicoCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado colocando el :class:`User` que esta
        utilizando la aplicación como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.director_medico.add(self.hospital.hospitalizacion)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class HospitalizadorCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado colocando el :class:`User` que esta
        utilizando la aplicación como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.hospitalizador.add(self.hospital.hospitalizacion)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class CirujanoCreateView(HospitalBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado colocando el :class:`User` que esta
        utilizando la aplicación como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.hospital.quirofano.cirujanos.add(self.object)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class HospitalUpdateView(UpdateView, LoginRequiredView):
    
    model = Hospital
    form_class = HospitalForm
    template_name = 'jqm/form.html'
    
    def get_context_data(self, **kwargs):
        
        context = super(HospitalUpdateView, self).get_context_data(**kwargs)
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

class TomografiaUpdateView(UpdateView, LoginRequiredView):
    
    model = Tomografia
    template_name = 'jqm/form.html'

class ResonanciaUpdateView(UpdateView, LoginRequiredView):
    
    model = ResonanciaMagenetica
    template_name = 'jqm/form.html'

class DensitometriaUpdateView(UpdateView, LoginRequiredView):
    
    model = Densitometria
    template_name = 'jqm/form.html'

class FluoroscopiaUpdateView(UpdateView, LoginRequiredView):
    
    model = Fluoroscopia
    template_name = 'jqm/form.html'

class MamografiaUpdateView(UpdateView, LoginRequiredView):
    
    model = Mamografia
    template_name = 'jqm/form.html'

class EcografiaUpdateView(UpdateView, LoginRequiredView):
    
    model = Ecografia
    template_name = 'jqm/form.html'

class ConsultorioCreateView(RedirectView):
    
    def get_context_data(self, **kwargs):
        
        context = super(ConsultorioCreateView, self).get_context_data(**kwargs)
        context['hospital'] = self.hospital
        return context
    
    def dispatch(self, *args, **kwargs):
        
        """Obtiene el :class:`Hospital` que se entrego como argumento en la
        url"""
        
        self.hospital = get_object_or_404(Hospital, pk=kwargs['hospital'])
        return super(ConsultorioCreateView, self).dispatch(*args, **kwargs)
    
    def get_redirect_url(self, **kwargs):
        
        """Obtiene la :class:`Dosis` desde la base de datos, la marca como
        suministrada, estampa la hora y el :class:`User` que la suministro"""
        
        consultorio = Consultorio()
        consultorio.hospital = self.hospital
        consultorio.save()
        return reverse('consultorio', args=[consultorio.id])

class ConsultorioBaseView(ContactoCreateView):
    
    def get_context_data(self, **kwargs):
        
        context = super(ConsultorioBaseView, self).get_context_data(**kwargs)
        context['consultorio'] = self.consultorio
        return context
    
    def dispatch(self, *args, **kwargs):
        
        """Obtiene el :class:`Consultorio` que se entrego como argumento en la
        url"""
        
        self.consultorio = get_object_or_404(Consultorio, pk=kwargs['consultorio'])
        return super(ConsultorioBaseView, self).dispatch(*args, **kwargs)
    
    def get_success_url(self):
        
        return reverse('consultorio', args=[self.consultorio.id])

class MedicoConsultorioCreateView(ConsultorioBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado colocando el :class:`User` que esta
        utilizando la aplicación como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.consultorios.add(self.consultorio)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class SecretariaConsultorioCreateView(ConsultorioBaseView):
    
    def form_valid(self, form):
        
        """Guarda el objeto generado colocando el :class:`User` que esta
        utilizando la aplicación como vendedor asignado a este contacto
        """
        
        self.object = form.save()
        self.object.secretaria_consultorio.add(self.consultorio)
        self.object.vendedores.add(self.request.user)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class ConsultorioDetailView(DetailView, LoginRequiredView):
    
    model = Consultorio
    context_object_name = 'consultorio'
