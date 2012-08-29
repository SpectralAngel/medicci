# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import permalink
from contactos.models import Hospital, Contacto

class Administracion(models.Model):
    
    hospital = models.OneToOneField(Hospital, primary_key=True, on_delete=models.CASCADE)
    propietario = models.ForeignKey(Contacto, null=True, blank=True, related_name="propietario")
    administrador = models.ForeignKey(Contacto, null=True, blank=True, related_name="administrador")
    jefe_de_compras = models.ForeignKey(Contacto, null=True, blank=True, related_name="jefe_de_compras")
    socios = models.ManyToManyField(Contacto)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'hospital', [self.hospital.id]

Hospital.administracion = property(lambda h: Administracion.objects.get_or_create(hospital=h)[0])

class Quirofano(models.Model):
    
    hospital = models.OneToOneField(Hospital, primary_key=True, on_delete=models.CASCADE)
    posee_quirofano = models.NullBooleanField()
    jefe = models.ForeignKey(Contacto, null=True, blank=True, related_name="jefe_quirofanos")
    licenciado = models.ForeignKey(Contacto, null=True, blank=True, related_name="licenciado_quirofanos")
    instrumentistas = models.ManyToManyField(Contacto, related_name="instrumentistas", null=True, blank=True)
    anestesiologos = models.ManyToManyField(Contacto, related_name="anestesiologos", null=True, blank=True)
    secretaria = models.ForeignKey(Contacto, null=True, blank=True, related_name="secretaria_quirofano")
    cirujanos = models.ManyToManyField(Contacto, related_name="cirujanos", null=True, blank=True)
    numero_de_quirofanos = models.IntegerField(default=0, blank=True)
    numero_de_salas_de_parto = models.IntegerField(default=0, blank=True)
    quirofanos_endoscopicos = models.IntegerField(default=0, blank=True)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'hospital', [self.hospital.id]

Hospital.quirofano = property(lambda h: Quirofano.objects.get_or_create(hospital=h)[0])

TIPOS_ANALISIS = (
    ('A', u'Análogo'),
    ('D', u'Digital'),
)

class CentroDeImagenes(models.Model):
    
    hospital = models.OneToOneField(Hospital, primary_key=True, on_delete=models.CASCADE)
    jefe = models.ForeignKey(Contacto, null=True, blank=True, related_name="jefe_imagenes")
    tecnicos = models.ManyToManyField(Contacto, related_name="tecnicos", null=True, blank=True)
    radiologos = models.ManyToManyField(Contacto, related_name="radiologos", null=True, blank=True)
    secretaria = models.ForeignKey(Contacto, null=True, blank=True, related_name="secretaria_imagenes")
    cantidad_de_equipos = models.IntegerField(default=0, blank=True)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'hospital', [self.hospital.id]

Hospital.centro_de_imagenes = property(lambda h: CentroDeImagenes.objects.get_or_create(hospital=h)[0])

class Tomografia(models.Model):
    
    centro_de_imagenes = models.OneToOneField(CentroDeImagenes, primary_key=True, on_delete=models.CASCADE)
    posee_tomografo = models.NullBooleanField()
    marca_tomografo = models.CharField(max_length=50, blank=True)
    piensa_aquirir_tomografo = models.CharField(max_length=50, blank=True)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'hospital', [self.hospital.id]

CentroDeImagenes.tomografia = property(lambda h: Tomografia.objects.get_or_create(centro_de_imagenes=h)[0])

class ResonanciaMagenetica(models.Model):
    
    centro_de_imagenes = models.OneToOneField(CentroDeImagenes, primary_key=True, on_delete=models.CASCADE)
    posee_resonancia_magnetica = models.NullBooleanField()
    piensa_aquirir_resonancia = models.CharField(max_length=50, blank=True)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'hospital', [self.hospital.id]

CentroDeImagenes.resonancia = property(lambda h: ResonanciaMagenetica.objects.get_or_create(centro_de_imagenes=h)[0])

class Fluoroscopia(models.Model):
    
    centro_de_imagenes = models.OneToOneField(CentroDeImagenes, primary_key=True, on_delete=models.CASCADE)
    posee_fluoroscopio = models.NullBooleanField()
    tipo_fluoroscopio = models.CharField(max_length=1, choices=TIPOS_ANALISIS, blank=True)
    piensa_aquirir_fluoroscopio = models.CharField(max_length=50, blank=True)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'hospital', [self.hospital.id]

CentroDeImagenes.fluoroscopia = property(lambda h: Fluoroscopia.objects.get_or_create(centro_de_imagenes=h)[0])

class Densitometria(models.Model):
    
    centro_de_imagenes = models.OneToOneField(CentroDeImagenes, primary_key=True, on_delete=models.CASCADE)
    posee_densitometro = models.NullBooleanField()
    tipo_densitometro = models.CharField(max_length=1, choices=TIPOS_ANALISIS, blank=True)
    piensa_aquirir_densitometro = models.CharField(max_length=50, blank=True)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'hospital', [self.hospital.id]

CentroDeImagenes.densitometria = property(lambda h: Densitometria.objects.get_or_create(centro_de_imagenes=h)[0])

class Mamografia(models.Model):
    
    centro_de_imagenes = models.OneToOneField(CentroDeImagenes, primary_key=True, on_delete=models.CASCADE)
    posee_mamografo = models.NullBooleanField()
    tipo_mamografo = models.CharField(max_length=1, choices=TIPOS_ANALISIS, blank=True)
    piensa_aquirir_mamografo = models.CharField(max_length=50, blank=True)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'hospital', [self.hospital.id]

CentroDeImagenes.mamografia = property(lambda h: Mamografia.objects.get_or_create(centro_de_imagenes=h)[0])

class Ecografia(models.Model):
    
    centro_de_imagenes = models.OneToOneField(CentroDeImagenes, primary_key=True, on_delete=models.CASCADE)
    posee_ultrasonido = models.NullBooleanField()
    cantidad_ultrasonidos = models.IntegerField(default=0, blank=True)
    algun_ultrasonido_4D = models.NullBooleanField()
    piensa_aquirir_ultrasonido = models.CharField(max_length=50, blank=True)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'hospital', [self.hospital.id]

CentroDeImagenes.Ecografia = property(lambda h: Ecografia.objects.get_or_create(centro_de_imagenes=h)[0])

class Hospitalizacion(models.Model):
    
    hospital = models.OneToOneField(Hospital, primary_key=True, on_delete=models.CASCADE)
    director_medico = models.ForeignKey(Contacto, null=True, blank=True, related_name="director_medico")
    hospitalizador = models.ForeignKey(Contacto, null=True, blank=True, related_name="hospitalizador")
    posee_hospitalizacion = models.NullBooleanField()
    cuantas_habitaciones_posee = models.IntegerField(default=0, blank=True)
    cuantas_habitaciones_dobles_posee = models.IntegerField(default=0, blank=True)
    cuantas_habitaciones_sencillas_posee = models.IntegerField(default=0, blank=True)
    cuantas_habitaciones_suite_posee = models.IntegerField(default=0, blank=True)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'hospital', [self.hospital.id]

Hospital.hospitalizacion = property(lambda h: Hospitalizacion.objects.get_or_create(hospital=h)[0])

class Consultorio(models.Model):
    
    hospital = models.ForeignKey(Hospital, related_name="consultorios")
    medico = models.ForeignKey(Contacto, null=True, blank=True, related_name="consultorios")
    secretaria = models.ForeignKey(Contacto, null=True, blank=True, related_name="secretaria_consultorio")
    
    @permalink
    def get_absolute_url(self):
        
        return 'consultorio', [self.id]
    
    def __unicode__(self):
        
        if self.medico != None:
            return u"{0} en {1}".format(self.medico, self.hospital)
        
        return u"{0}".format(self.hospital)
