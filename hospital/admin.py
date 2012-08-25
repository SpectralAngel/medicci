# -*- coding: utf-8 -*-
from django.contrib import admin
from hospital.models import (Administracion, CentroDeImagenes, CentroTecnico,
                             Hospitalizacion, Quirofano)

admin.site.register(Administracion)
admin.site.register(CentroDeImagenes)
admin.site.register(CentroTecnico)
admin.site.register(Hospitalizacion)
admin.site.register(Quirofano)
