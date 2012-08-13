# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.utils import timezone
from datetime import timedelta, datetime
from contactos.models import Cita
from django.contrib.auth.models import User

class IndexView(TemplateView):
    
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        
        context = super(IndexView, self).get_context_data(**kwargs)
        today = timezone.now()
        today = datetime(today.year, today.month, today.day)
        timezone.make_aware(today, timezone.get_current_timezone())
        later = timezone.make_aware(today + timedelta(31), timezone.get_current_timezone())
        context['citas'] = Cita.objects.filter(
            fecha_y_hora__gte=today,
            usuario=self.request.user
        ).exclude(
            fecha_y_hora__gte=later,
        ).exclude(
            visitada = True
        )
        return context
