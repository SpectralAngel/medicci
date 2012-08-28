# -*- coding: utf-8 -*-
from django.contrib import admin
from contactos.models import (Contacto, Especialidad, Cita, Ciclo, Departamento,
                              Zona, Municipio, Direccion, Telefono, Email,
                              Visita, Hospital, Material, Producto,
                              MaterialUtilizado, Asociacion, BBPin, Profile)

admin.site.register(Contacto)
admin.site.register(Cita)
admin.site.register(Ciclo)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Direccion)
admin.site.register(Telefono)
admin.site.register(Email)
admin.site.register(Visita)
admin.site.register(Material)
admin.site.register(MaterialUtilizado)
admin.site.register(Producto)
admin.site.register(Especialidad)
admin.site.register(Asociacion)
admin.site.register(Hospital)
admin.site.register(Zona)
admin.site.register(BBPin)
admin.site.register(Profile)
