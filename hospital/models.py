# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import permalink
from contactos.models import Hospital

class Administracion(models.Model):
    
    hospital = models.OneToOneField(Hospital, primary_key=True)
    propietario = models.CharField(max_length=50, blank=True)
    administrador = models.CharField(max_length=50, blank=True)
    jefe_de_compras = models.CharField(max_length=50, blank=True)
    socios = models.TextField(blank=True)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'hospital', [self.hospital.id]

Hospital.administracion = property(lambda h: Administracion.objects.get_or_create(hospital=h)[0])

class Quirofano(models.Model):
    
    hospital = models.OneToOneField(Hospital, primary_key=True)
    posee_quirofano = models.NullBooleanField()
    jefe = models.CharField(max_length=50, blank=True)
    instrumentista = models.CharField(max_length=50, blank=True)
    secretaria = models.CharField(max_length=50, blank=True)
    doctores = models.TextField(blank=True)
    numero_de_quirofanos = models.IntegerField(default=0, blank=True)
    numero_de_salas_de_parto = models.IntegerField(default=0, blank=True)
    quirofanos_endoscopicos = models.IntegerField(default=0, blank=True)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'hospital', [self.hospital.id]

Hospital.quirofano = property(lambda h: Quirofano.objects.get_or_create(hospital=h)[0])

class CentroDeImagenes(models.Model):
    
    TIPOS_ANALISIS = (
        ('A', u'Análogo'),
        ('D', u'Digital'),
    )
    
    hospital = models.OneToOneField(Hospital, primary_key=True)
    cantidad_de_equipos = models.IntegerField(default=0, blank=True)
    posee_tomografo = models.NullBooleanField()
    marca_tomografo = models.CharField(max_length=50, blank=True)
    piensa_aquirir_tomografo = models.CharField(max_length=50, blank=True)
    posee_resonancia_magnetica = models.NullBooleanField()
    piensa_aquirir_resonancia = models.CharField(max_length=50, blank=True)
    posee_fluoroscopio = models.NullBooleanField()
    tipo_fluoroscopio = models.CharField(max_length=1, choices=TIPOS_ANALISIS, blank=True)
    piensa_aquirir_fluoroscopio = models.CharField(max_length=50, blank=True)
    posee_densitometro = models.NullBooleanField()
    tipo_densitometro = models.CharField(max_length=1, choices=TIPOS_ANALISIS, blank=True)
    piensa_aquirir_densitometro = models.CharField(max_length=50, blank=True)
    posee_mamografo = models.NullBooleanField()
    tipo_mamografo = models.CharField(max_length=1, choices=TIPOS_ANALISIS, blank=True)
    piensa_aquirir_mamografo = models.CharField(max_length=50, blank=True)
    posee_ultrasonido = models.NullBooleanField()
    cantidad_ultrasonidos = models.IntegerField(default=0, blank=True)
    algun_ultrasonido_4D = models.NullBooleanField()
    piensa_aquirir_ultrasonido = models.CharField(max_length=50, blank=True)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'hospital', [self.hospital.id]

Hospital.centro_de_imagenes = property(lambda h: CentroDeImagenes.objects.get_or_create(hospital=h)[0])

class CentroTecnico(models.Model):
    
    hospital = models.OneToOneField(Hospital, primary_key=True)
    jefe = models.CharField(max_length=50, blank=True)
    tecnicos = models.TextField(blank=True)
    radiologos = models.TextField(blank=True)
    secretaria = models.CharField(max_length=50, blank=True)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'hospital', [self.hospital.id]

Hospital.centro_tecnico = property(lambda h: CentroTecnico.objects.get_or_create(hospital=h)[0])

class Hospitalizacion(models.Model):
    
    hospital = models.OneToOneField(Hospital, primary_key=True)
    posee_hospitalizacion = models.NullBooleanField()
    cuantas_habitaciones_posee = models.IntegerField(default=0, blank=True)
    cuantas_habitaciones_dobles_posee = models.IntegerField(default=0, blank=True)
    cuantas_habitaciones_sencillas_posee = models.IntegerField(default=0, blank=True)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'hospital', [self.hospital.id]

Hospital.hospitalizacion = property(lambda h: Hospitalizacion.objects.get_or_create(hospital=h)[0])
