# -*- coding: utf-8 -*-
from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink
from django.db.models.query_utils import Q
from django.utils import timezone

class Ciclo(models.Model):
    
    nombre = models.CharField(max_length=50, blank=True)
    inicio = models.DateField(default=date.today)
    fin = models.DateField(default=date.today)
    
    def __unicode__(self):
        
        return u"{0}".format(self.nombre)

class Departamento(models.Model):
    
    nombre = models.CharField(max_length=50, blank=True)
    
    def __unicode__(self):
        
        return u"{0}".format(self.nombre)

class Municipio(models.Model):
    
    departamento = models.ForeignKey(Departamento, related_name="municipios")
    nombre = models.CharField(max_length=50, blank=True)
    
    def __unicode__(self):
        
        return u"{0}, {1}".format(self.departamento.nombre, self.nombre)

class Especialidad(models.Model):
    
    """Define las Especialidades a las que pertenece el Doctor"""
    
    nombre = models.CharField(max_length=200, blank=True)
    
    def __unicode__(self):
        
        return u"{0}".format(self.nombre)

class Asociacion(models.Model):
    
    nombre = models.CharField(max_length=200, blank=True)
    
    def __unicode__(self):
        
        return u"{0}".format(self.nombre)

class Zona(models.Model):
    
    nombre = models.CharField(max_length=50)
    
    def __unicode__(self):
        
        return u"{0}".format(self.nombre)

class Hospital(models.Model):
    
    TIPOS_DE_HOSPITAL = (
        ('P', u'Privado'),
        ('G', u'Público'),
        ('C', u'Clínica'),
        ('I', u'Centro de Imágenes'),
        ('L', u'Laboratorio'),
    )
    
    zona = models.ForeignKey(Zona, related_name='hospitales')
    municipio = models.ForeignKey(Municipio, related_name='hospitales')
    nombre = models.CharField(max_length=200)
    numero = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    tipo_hospital = models.CharField(max_length=2, choices=TIPOS_DE_HOSPITAL)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'hospital', [self.id]
    
    def __unicode__(self):
        
        return u"{0}".format(self.nombre)

class Cuenta(models.Model):
    
    hospital = models.ForeignKey(Hospital, related_name="cuentas")
    nombre = models.CharField(max_length=200, blank=True)
    
    def __unicode__(self):
        
        return u"{0} de {1}".format(self.nombre, self.hospital.nombre)
    
class Contacto(models.Model):
    
    SEXOS = (
        ('M', u'Masculino'),
        ('F', u'Femenino'),
    )
    
    TURNOS =(
        ('N', 'Ninguno'),
        ('M', 'Mañana'),
        ('T', 'Tarde'),
    )
    
    TITULOS = (
        ('Sr.', u'Señor'),
        ('Sra.', u'Señora'),
        ('Srita.', u'Señorita'),
        ('Dr.', u'Doctor/a'),
        ('Lic.', u'Licenciado/a'),
        ('Ing.', u'Ingeniero/a'),
        ('Arq.', u'Arquitecto/a'),
        ('Abg.', u'Abogado/a'),
    )
    
    titulo = models.CharField(max_length=6, choices=TITULOS, blank=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=SEXOS)
    nacimiento = models.DateField(default=date.today, blank=True)
    web = models.CharField(max_length=200, blank=True)
    horario = models.CharField(max_length=1, choices=TURNOS, blank=True)
    ciudad = models.ForeignKey(Municipio, related_name="contactos", blank=True)
    especialidades = models.ManyToManyField(Especialidad,
                                           related_name="contactos", blank=True)
    hospitales = models.ManyToManyField(Hospital, related_name="contactos")
    vendedores = models.ManyToManyField(User, related_name='contactos')
    asociaciones = models.ManyToManyField(Asociacion, related_name='contactos')
    agregado = models.DateField(default=date.today)
    activo = models.BooleanField(default=True)
    email = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=50, default='')
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'contacto-ver', [self.id]
    
    def __unicode__(self):
        
        return u"{0} {1}".format(self.nombre, self.apellido)
    
    @staticmethod
    def get_queryset(params):
        
        """Construye un :clas:`QuerySet` de manera dinámica para efectuar
        búsquedas"""
        
        nombre = params.get('nombre')
        apellido = params.get('apellido')
        cuentas = params.get('cuentas')
        especialidades = params.get('especialidades')
        ciudad = params.get('ciudad')
        qset = Q(pk__gt = 0)
        
        if nombre:
            qset &= Q(nombre__icontains = nombre)
        if apellido:
            qset &= Q(apellido__icontains = apellido)
        if ciudad:
            qset &= Q(ciudad__id = ciudad)
        if cuentas:
            qset &= Q(cuenta__id__in = [c for c in cuentas])
        if especialidades:
            qset &= Q(especialidad__id__in = [e for e in especialidades])
        
        return qset

class Clinica(models.Model):
    
    contacto = models.ForeignKey(Contacto, related_name="clinicas")
    direccion = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=200, blank=True)
    fax = models.CharField(max_length=200, blank=True)

class Direccion(models.Model):
    
    TIPO_DIRECCION = (
        ('O', u'Oficina'),
        ('CI', u'Centro de Imágenes'),
        ('L', u'Laboratorio'),
        ('C', u'Consultorio'),
        ('CP', u'Clínica Privada'),
    )
    
    contacto = models.ForeignKey(Contacto, related_name="direcciones")
    calle = models.TextField(blank=True, null=True)
    ciudad = models.ForeignKey(Municipio, related_name="direcciones")
    departamento = models.ForeignKey(Departamento, related_name="direcciones")
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'contacto-ver', [self.contacto.id]
    
    def __unicode__(self):
        
        return u"{0} {1}, {2}".format(self.calle, self.ciudad.nombre,
                                     self.departamento.nombre)

class Telefono(models.Model):
    
    TIPOS = (
        ('C', u'Casa'),
        ('T', u'Trabajo'),
        ('F', u'Fax'),
        ('M', u'Móvil'),
        ('O', u'Otro'),
    )
    
    contacto = models.ForeignKey(Contacto, related_name="telefonos")
    tipo = models.CharField(max_length=1, choices=TIPOS, blank=True)
    numero = models.CharField(max_length=200, blank=True)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'contacto-ver', [self.contacto.id]
    
    def __unicode__(self):
        
        return u"{0}".format(self.numero)

class Email(models.Model):
    
    TIPOS_EMAIL = (
        ('C', u'Casa'),
        ('T', u'Trabajo'),
        ('O', u'Otro'),
    )
    
    contacto = models.ForeignKey(Contacto, related_name="emails")
    tipo = models.CharField(max_length=1, choices=TIPOS_EMAIL, blank=True)
    correo = models.EmailField()
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'contacto-ver', [self.contacto.id]
    
    def __unicode__(self):
        
        return u"{0}".format(self.correo)

class BBPin(models.Model):
    
    TIPOS_PIN = (
        ('C', u'Personal'),
        ('T', u'Trabajo'),
        ('O', u'Otro'),
    )
    
    contacto = models.ForeignKey(Contacto, related_name="bbpins")
    numero = models.CharField(max_length=200, blank=True)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'contacto-ver', [self.contacto.id]
    
    def __unicode__(self):
        
        return u"{0}".format(self.correo)

class Producto(models.Model):
    
    nombre = models.CharField(max_length=200, blank=True)
    marca = models.CharField(max_length=200, blank=True)
    descripcion = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        
        return u"{0} - {1}".format(self.nombre, self.marca)

class Material(models.Model):
    
    nombre = models.CharField(max_length=200, blank=True)
    
    def __unicode__(self):
        
        return u"{0}".format(self.nombre)

class Cita(models.Model):
    
    contacto = models.ForeignKey(Contacto, related_name="citas")
    fecha_y_hora = models.DateTimeField(default=timezone.now)
    fin = models.DateTimeField(default=timezone.now)
    visitada = models.NullBooleanField(blank=True, null=True)
    usuario = models.ForeignKey(User, blank=True, null=True,
                                   related_name='citas')
    motivo = models.TextField(blank=True, null=True)
    publicada = models.BooleanField(default=False)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'cita-ver', [self.id]
    
    def __unicode__(self):
        
        return u"{0} {1}".format(self.contacto, self.fecha_y_hora)
    
    def as_event(self):
        
        title = self.contacto
        fecha = "new Date({0}, {1}, {2}, {3}, {4})".format(
                self.fecha_y_hora.year,
                self.fecha_y_hora.month,
                self.fecha_y_hora.day,
                self.fecha_y_hora.hour,
                self.fecha_y_hora.minute
        )
        final = "new Date({0}, {1}, {2}, {3}, {4})".format(
                self.final.year,
                self.final.month,
                self.final.day,
                self.final.hour,
                self.final.minute
        )
        
        return "{title: {0}, start: {1}, end: {2},}".format(title, fecha, final)

class Visita(models.Model):
    
    contacto = models.ForeignKey(Contacto, related_name="visitas")
    fecha_y_hora = models.DateTimeField(default=timezone.now)
    fin = models.DateTimeField(default=timezone.now)
    comentarios = models.TextField(blank=True, null=True)
    productos = models.ManyToManyField(Producto, related_name="visitas",
                                       blank=True)
    usuario = models.ForeignKey(User, blank=True, null=True,
                                related_name='visitas')
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'visita-ver', [self.id]
    
    def __unicode__(self):
        
        return u"{0} {1}".format(self.contacto, self.fecha_y_hora)
    
    def costo(self):
        
        return sum(m.costo for m in self.materiales.all())

class MaterialUtilizado(models.Model):
    
    visita = models.ForeignKey(Visita, related_name="materiales")
    material = models.ForeignKey(Material, related_name="utlizado")
    costo = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'visita-ver', [self.visita.id]
    
    def __unicode__(self):
        
        return u"{0} {1}".format(self.material, self.costo)

class Venta(models.Model):
    
    cuenta = models.ForeignKey(Cuenta, related_name='ventas')
    producto = models.ForeignKey(Producto, related_name='ventas')
    fecha = models.DateField(default=date.today)
    vendedor = models.ForeignKey(User, blank=True, null=True,
                                   related_name='ventas')

class Profile(models.Model):
    
    user = models.OneToOneField(User, primary_key=True)
    zona = models.ForeignKey(Zona, related_name='perfiles', blank=True, null=True)
    telefono = models.CharField(max_length=200, blank=True)
    skype = models.CharField(max_length=200, blank=True)
    fecha_de_nacimiento = models.DateField(default=date.today) 
    configurado = models.BooleanField(default=False)
    
    @permalink
    def get_absolute_url(self):
        
        """Obtiene la URL absoluta"""
        
        return 'profile', []

    def __unicode__(self):
        
        return self.user.username

User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
