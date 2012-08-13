# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.views.generic import (ListView, UpdateView, DetailView, CreateView,
                                  RedirectView, View, TemplateView)
from django.contrib import messages
from django.utils import timezone
from contactos.models import (Contacto, Especialidad, Cita, Horario, Ciclo,
                            Departamento, Municipio, Direccion, Telefono, Email,
                            Visita, Material, MaterialUtilizado)
from medicci.contactos.forms import (ContactoForm, VisitaForm, CitaForm,
                            TelefonoForm, EmailForm, DireccionForm,
                            MaterialUtilizadoForm)

class LoginRequiredView(View):
    
    """Clase base para crear vistas que requieren inicio de sesión"""
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        
        """Permite despachar la petición en caso que el usuario tenga iniciada
        su sesión en la aplicación"""
        
        return super(LoginRequiredView, self).dispatch(request, *args, **kwargs)

class ContactoIndexView(ListView, LoginRequiredView):
    
    context_object_name = 'contactos'
    
    def get_queryset(self):
        
        return self.request.user.contactos.all()
    
class ContactoCreateView(CreateView, LoginRequiredView):
    
    model = Contacto
    form_class = ContactoForm
    template_name = 'jqm/form.html'

    def get_context_data(self, **kwargs):
        
        context = super(ContactoCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Medicci - Agregar Contacto"
        return context

class ContactoUpdateView(UpdateView, LoginRequiredView):
    
    model = Contacto
    form_class = ContactoForm
    
    template_name = 'jqm/form.html'

    def get_context_data(self, **kwargs):
        
        context = super(ContactoUpdateView, self).get_context_data(**kwargs)
        context['title'] = u"Medicci - Actualizar Contacto"
        return context
        
class ContactoDetailView(DetailView, LoginRequiredView):
        
    model = Contacto
    context_object_name = 'contacto'
    
class BaseCreateView(CreateView, LoginRequiredView):
    
    """Permite llenar el formulario de una clase que requiera
    :class:`Contacto`s y :class:`User`s de manera previa"""

    def get_context_data(self, **kwargs):
        
        context = super(BaseCreateView, self).get_context_data(**kwargs)
        context['contacto'] = self.contacto
        return context
    
    def get_form_kwargs(self):
        
        """Agrega la :class:`contacto` obtenida como el valor a utilizar en el
        formulario que será llenado posteriormente"""

        kwargs = super(BaseCreateView, self).get_form_kwargs()
        kwargs.update({'initial':{'contacto':self.contacto.id,
                                  'fecha_y_hora': timezone.now(),
                                  'usuario':self.request.user.id}})
        return kwargs
    
    def dispatch(self, *args, **kwargs):
        
        """Obtiene la :class:`contacto` que se entrego como argumento en la
        url"""

        self.contacto = get_object_or_404(Contacto, pk=kwargs['contacto'])
        return super(BaseCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        
        """Guarda el objeto generado espeficando la :class:`contacto` obtenida
        de los argumentos y el :class:`User` que esta utilizando la aplicación
        """

        self.object = form.save(commit=False)
        self.object.contacto = self.contacto
        self.usuario = self.request.user
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class CitaDetailView(DetailView, LoginRequiredView):
    
    model = Cita
    context_object_name = 'cita'

class CitaCreateView(BaseCreateView):
    
    model = Cita
    form_class = CitaForm
    template_name = 'jqm/form.html'

    def get_context_data(self, **kwargs):
        
        context = super(CitaCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Agendar Cita a {0}".format(self.contacto)
        return context

class CitaUpdateView(UpdateView):
    
    model = Cita
    form_class = CitaForm
    template_name = 'jqm/form.html'

class CitaVisitarView(RedirectView, LoginRequiredView):

    """Indica que una :class:`Cita` ya ha sido efectuada"""
     
    permanent = False
    
    def get_redirect_url(self, **kwargs):
        
        cita = get_object_or_404(Cita, pk=kwargs['pk'])
        cita.visitada = True
        cita.save()
        messages.info(self.request, u'¡La cita ha sido efectuada!')
        return reverse('visita-agregar', args=[cita.contacto.id])

class VisitaDetailView(DetailView, LoginRequiredView):
    
    model = Visita
    context_object_name = 'visita'
    
class VisitaCreateView(BaseCreateView):
    
    model = Visita
    form_class = VisitaForm
    template_name = 'jqm/form.html'

    def get_context_data(self, **kwargs):
        
        context = super(VisitaCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Registrar Visita a {0}".format(self.contacto)
        return context

class VisitaUpdateView(UpdateView):
    
    model = Visita
    form_class = VisitaForm
    template_name = 'jqm/form.html'

class MaterialUtilizadoCreateView(CreateView, LoginRequiredView):
    
    model = MaterialUtilizado
    form_class = MaterialUtilizadoForm
    template_name = 'jqm/form.html'

    def get_context_data(self, **kwargs):
        
        context = super(MaterialUtilizadoCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Agregar Material a Visita a {0}".format(self.visita.contacto)
        context['visita'] = self.visita
        return context
    
    def get_form_kwargs(self):
        
        """Agrega la :class:`Visita` obtenida como el valor a utilizar en el
        formulario que será llenado posteriormente"""

        kwargs = super(MaterialUtilizadoCreateView, self).get_form_kwargs()
        kwargs.update({'initial':{'visita':self.visita.id}})
        return kwargs
    
    def dispatch(self, *args, **kwargs):
        
        """Obtiene la :class:`Visita` que se entrego como argumento en la
        url"""

        self.visita = get_object_or_404(Visita, pk=kwargs['visita'])
        return super(MaterialUtilizadoCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        
        """Guarda el objeto generado espeficando la :class:`Visita` obtenida
        de los argumentos"""

        self.object = form.save(commit=False)
        self.object.visita = self.visita
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class BaseContactoCreateView(CreateView, LoginRequiredView):
    
    """Permite llenar el formulario de una clase que requiera
    :class:`Contacto`s de manera previa - DRY"""
    
    template_name = 'jqm/form.html'

    def get_context_data(self, **kwargs):
        
        context = super(BaseContactoCreateView, self).get_context_data(**kwargs)
        context['contacto'] = self.contacto
        return context
    
    def get_form_kwargs(self):
        
        """Agrega la :class:`contacto` obtenida como el valor a utilizar en el
        formulario que será llenado posteriormente"""

        kwargs = super(BaseContactoCreateView, self).get_form_kwargs()
        kwargs.update({'initial':{'contacto':self.contacto.id,
                                  'fecha_y_hora': timezone.now(),
                                  'usuario':self.request.user.id}})
        return kwargs
    
    def dispatch(self, *args, **kwargs):
        
        """Obtiene la :class:`contacto` que se entrego como argumento en la
        url"""

        self.contacto = get_object_or_404(Contacto, pk=kwargs['contacto'])
        return super(BaseContactoCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        
        """Guarda el objeto generado espeficando la :class:`contacto` obtenida
        de los argumentos y el :class:`User` que esta utilizando la aplicación
        """

        self.object = form.save(commit=False)
        self.object.contacto = self.contacto
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

class TelefonoCreateView(BaseContactoCreateView):
    
    model = Telefono
    form_class = TelefonoForm

class EmailCreateView(BaseContactoCreateView):
    
    model = Email
    form_class = EmailForm

class DireccionCreateView(BaseContactoCreateView):
    
    model = Direccion
    form_class = DireccionForm
