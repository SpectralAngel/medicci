# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from hospital.views import (HospitalCreateView, HospitalDetailView, HospitalUpdateView,
    AdministracionUpdateView, CentroDeImagenesUpdateView, CentroTecnicoUpdateView,
    HospitalizacionUpdateView, QuirofanoUpdateView, PropietarioCreateView,
    JefeComprasCreateView, AdministradorCreateView, JefeQuirofanoCreateView,
    SecretariaQuirofanoCreateView, JefeTecnicoCreateView,
    SecretariaTecnicoCreateView, InstrumentistaCreateView, SocioCreateView)

urlpatterns = patterns('',
    
    url(r'^agregar/zona/(?P<zona>\d+)$',
        HospitalCreateView.as_view(), name='hospital-agregar'),
    
    url(r'^(?P<pk>\d+)$',
        HospitalDetailView.as_view(), name='hospital'),
    
    url(r'^(?P<pk>\d+)/editar$',
        HospitalUpdateView.as_view(), name='hospital-editar'),
    
    url(r'^administracion/(?P<pk>\d+)/editar$',
        AdministracionUpdateView.as_view(), name='administracion-editar'),
    
    url(r'^administracion/(?P<hospital>\d+)/propietario$',
        PropietarioCreateView.as_view(), name='propietario-agregar'),
    
    url(r'^administracion/(?P<hospital>\d+)/compra$',
        JefeComprasCreateView.as_view(), name='compras-agregar'),
    
    url(r'^administracion/(?P<hospital>\d+)/socio$',
        SocioCreateView.as_view(), name='agregar-socio'),
    
    url(r'^administracion/(?P<hospital>\d+)/administrador$',
        AdministradorCreateView.as_view(), name='administrador-agregar'),
    
    url(r'^administracion/(?P<pk>\d+)/editar$',
        AdministracionUpdateView.as_view(), name='administracion-editar'),
    
    url(r'^imagenes/(?P<pk>\d+)/editar$',
        CentroDeImagenesUpdateView.as_view(), name='imagenes-editar'),
    
    url(r'^tecnico/(?P<pk>\d+)/editar$',
        CentroTecnicoUpdateView.as_view(), name='tecnico-editar'),
    
    url(r'^tecnico/(?P<hospital>\d+)/jefe$',
        JefeTecnicoCreateView.as_view(), name='jefe-tecnico-agregar'),
    
    url(r'^tecnico/(?P<hospital>\d+)/jefe$',
        SecretariaTecnicoCreateView.as_view(), name='secretaria-tecnico-agregar'),
    
    url(r'^hospitalizacion/(?P<pk>\d+)/editar$',
        HospitalizacionUpdateView.as_view(), name='hospitalizacion-editar'),
    
    url(r'^quirofano/(?P<pk>\d+)/editar$',
        QuirofanoUpdateView.as_view(), name='quirofano-editar'),
    
    url(r'^quirofano/(?P<hospital>\d+)/jefe$',
        JefeQuirofanoCreateView.as_view(), name='jefe-quirofano-agregar'),
    
    url(r'^quirofano/(?P<hospital>\d+)/secretaria$',
        SecretariaQuirofanoCreateView.as_view(), name='secretaria-quirofano-agregar'),
    
    url(r'^quirofano/(?P<hospital>\d+)/instrumentista$',
        InstrumentistaCreateView.as_view(), name='instrumentista-quirofano-agregar'),
)
