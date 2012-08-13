# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from contactos.views import (
  ContactoCreateView, ContactoDetailView, ContactoIndexView, ContactoUpdateView,
  VisitaCreateView, VisitaDetailView, VisitaUpdateView, 
  CitaCreateView, CitaDetailView, CitaVisitarView, CitaUpdateView,
  TelefonoCreateView, EmailCreateView, MaterialUtilizadoCreateView,
  DireccionCreateView)

urlpatterns = patterns('',
    
    url(r'^$',
        ContactoIndexView.as_view(), name='mis-contactos'),
    
    url(r'^agregar$',
        ContactoCreateView.as_view(), name='contacto-agregar'),
    
    url(r'^(?P<pk>\d+)$',
        ContactoDetailView.as_view(), name='contacto-ver'),
    
    url(r'^(?P<pk>\d+)/editar$',
        ContactoUpdateView.as_view(), name='contacto-editar'),
    
    url(r'^cita/(?P<pk>\d+)$',
        CitaDetailView.as_view(), name='cita-ver'),
    
    url(r'^visita/(?P<pk>\d+)$',
        VisitaDetailView.as_view(), name='visita-ver'),
    
    url(r'^(?P<contacto>\d+)/cita/agregar$',
        CitaCreateView.as_view(), name='cita-agregar'),
    
    url(r'^cita/(?P<pk>\d+)/visitar$',
        CitaVisitarView.as_view(), name='cita-visitar'),
    
    url(r'^cita/(?P<pk>\d+)/editar$',
        CitaUpdateView.as_view(), name='cita-editar'),
    
    url(r'^(?P<contacto>\d+)/visita/agregar$',
        VisitaCreateView.as_view(), name='visita-agregar'),
    
    url(r'^visita/(?P<pk>\d+)/editar$',
        VisitaUpdateView.as_view(), name='visita-editar'),
    
    url(r'^(?P<visita>\d+)/material/agregar$',
        MaterialUtilizadoCreateView.as_view(), name='material-utilizar'),
    
    url(r'^(?P<contacto>\d+)/telefono/agregar$',
        TelefonoCreateView.as_view(), name='telefono-agregar'),
    
    url(r'^(?P<contacto>\d+)/direccion/agregar$',
        DireccionCreateView.as_view(), name='direccion-agregar'),
    
    url(r'^(?P<contacto>\d+)/email/agregar$',
        EmailCreateView.as_view(), name='email-agregar'),
)
