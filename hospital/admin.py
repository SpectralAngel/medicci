# -*- coding: utf-8 -*-
from django.contrib import admin
from hospital.models import (Administracion, CentroDeImagenes, Hospitalizacion,
                             Quirofano)

admin.site.register(Administracion)
admin.site.register(CentroDeImagenes)
admin.site.register(Hospitalizacion)
admin.site.register(Quirofano)
