# -*- coding: utf-8 -*-
from django.contrib import admin
from hospital.models import (Administracion, CentroDeImagenes, Hospitalizacion,
                             Quirofano, Consultorio)

admin.site.register(Administracion)
admin.site.register(CentroDeImagenes)
admin.site.register(Hospitalizacion)
admin.site.register(Quirofano)
admin.site.register(Consultorio)
