# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from hospital.views import (HospitalCreateView, HospitalDetailView, HospitalUpdateView,
    AdministracionUpdateView, CentroDeImagenesUpdateView, CentroTecnicoUpdateView,
    HospitalizacionUpdateView, QuirofanoUpdateView)

urlpatterns = patterns('',
    
    url(r'^agregar/zona/(?P<zona>\d+)$',
        HospitalCreateView.as_view(), name='hospital-agregar'),
    
    url(r'^(?P<pk>\d+)$',
        HospitalDetailView.as_view(), name='hospital'),
    
    url(r'^(?P<pk>\d+)/editar$',
        HospitalUpdateView.as_view(), name='hospital-editar'),
    
    url(r'^administracion/(?P<pk>\d+)/editar$',
        AdministracionUpdateView.as_view(), name='administracion-editar'),
    
    url(r'^imagenes/(?P<pk>\d+)/editar$',
        CentroDeImagenesUpdateView.as_view(), name='imagenes-editar'),
    
    url(r'^tecnico/(?P<pk>\d+)/editar$',
        CentroTecnicoUpdateView.as_view(), name='tecnico-editar'),
    
    url(r'^hospitalizacion/(?P<pk>\d+)/editar$',
        HospitalizacionUpdateView.as_view(), name='hospitalizacion-editar'),
    
    url(r'^quirofano/(?P<pk>\d+)/editar$',
        QuirofanoUpdateView.as_view(), name='quirofano-editar'),
)
