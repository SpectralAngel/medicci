# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from hospital.views import (HospitalCreateView, HospitalDetailView, HospitalUpdateView,
    AdministracionUpdateView, CentroDeImagenesUpdateView,
    HospitalizacionUpdateView, QuirofanoUpdateView, PropietarioCreateView,
    JefeComprasCreateView, AdministradorCreateView, JefeQuirofanoCreateView,
    SecretariaQuirofanoCreateView, JefeImagenesCreateView,
    SecretariaImagenesCreateView, InstrumentistaCreateView, SocioCreateView,
    DirectorMedicoCreateView, HospitalizadorCreateView, CirujanoCreateView,
    LicenciadoQuirofanoCreateView, RadiologoCreateView, TecnicoCreateView,
    TomografiaUpdateView, MamografiaUpdateView, EcografiaUpdateView,
    FluoroscopiaUpdateView, DensitometriaUpdateView, ResonanciaUpdateView,
    ConsultorioCreateView, ConsultorioDetailView, MedicoConsultorioCreateView,
    SecretariaConsultorioCreateView)

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
    
    url(r'^imagenes/(?P<pk>\d+)/tomografia/editar$',
        TomografiaUpdateView.as_view(), name='tomografia-editar'),
    
    url(r'^imagenes/(?P<pk>\d+)/mamografia/editar$',
        MamografiaUpdateView.as_view(), name='mamografia-editar'),
    
    url(r'^imagenes/(?P<pk>\d+)/ecografia/editar$',
        EcografiaUpdateView.as_view(), name='ecografia-editar'),
    
    url(r'^imagenes/(?P<pk>\d+)/fluoroscopia/editar$',
        FluoroscopiaUpdateView.as_view(), name='fluoroscopia-editar'),
    
    url(r'^imagenes/(?P<pk>\d+)/densitometria/editar$',
        DensitometriaUpdateView.as_view(), name='densitometria-editar'),
    
    url(r'^imagenes/(?P<pk>\d+)/resonancia/editar$',
        ResonanciaUpdateView.as_view(), name='resonancia-editar'),
    
    url(r'^imagenes/(?P<hospital>\d+)/jefe$',
        JefeImagenesCreateView.as_view(), name='jefe-imagenes-agregar'),
    
    url(r'^imagenes/(?P<hospital>\d+)/radiologo',
        RadiologoCreateView.as_view(), name='radiologo-agregar'),
    
    url(r'^imagenes/(?P<hospital>\d+)/tecnico',
        TecnicoCreateView.as_view(), name='tecnico-imagenes-agregar'),
    
    url(r'^imagenes/(?P<hospital>\d+)/jefe$',
        SecretariaImagenesCreateView.as_view(), name='secretaria-imagenes-agregar'),
    
    url(r'^hospitalizacion/(?P<hospital>\d+)/director$',
        DirectorMedicoCreateView.as_view(), name='director-medico-agregar'),
    
    url(r'^hospitalizacion/(?P<hospital>\d+)/hospitalizador$',
        HospitalizadorCreateView.as_view(), name='hospitalizador-agregar'),
    
    url(r'^hospitalizacion/(?P<pk>\d+)/editar$',
        HospitalizacionUpdateView.as_view(), name='hospitalizacion-editar'),
    
    url(r'^quirofano/(?P<pk>\d+)/editar$',
        QuirofanoUpdateView.as_view(), name='quirofano-editar'),
    
    url(r'^quirofano/(?P<hospital>\d+)/jefe$',
        JefeQuirofanoCreateView.as_view(), name='jefe-quirofano-agregar'),
    
    url(r'^quirofano/(?P<hospital>\d+)/licenciado$',
        LicenciadoQuirofanoCreateView.as_view(), name='licenciado-quirofano-agregar'),
    
    url(r'^quirofano/(?P<hospital>\d+)/secretaria$',
        SecretariaQuirofanoCreateView.as_view(), name='secretaria-quirofano-agregar'),
    
    url(r'^quirofano/(?P<hospital>\d+)/instrumentista$',
        InstrumentistaCreateView.as_view(), name='instrumentista-quirofano-agregar'),
    
    url(r'^quirofano/(?P<hospital>\d+)/cirujano$',
        CirujanoCreateView.as_view(), name='cirujano-quirofano-agregar'),
    
    url(r'^consultorio/(?P<hospital>\d+)/agregar$',
        ConsultorioCreateView.as_view(), name='consultorio-agregar'),
    
    url(r'^consultorio/(?P<pk>\d+)$',
        ConsultorioDetailView.as_view(), name='consultorio'),
    
    url(r'^consultorio/(?P<consultorio>\d+)/medico$',
        MedicoConsultorioCreateView.as_view(), name='medico-consultorio-agregar'),
    
    url(r'^consultorio/(?P<consultorio>\d+)/secretaria$',
        SecretariaConsultorioCreateView.as_view(), name='secretaria-consultorio-agregar'),
)
