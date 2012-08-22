# -*- coding: utf-8 -*-
from django import forms

class BasicDateBox(forms.DateInput):
    
    input_type = 'date'
    
    def __init__(self, attrs=None):
        super(BasicDateBox, self).__init__(attrs)
        if attrs is not None:
            self.attrs = attrs.copy()
        
        self.attrs['data-role'] = 'datebox'
        
        if not 'format' in self.attrs:
            self.attrs['format'] = '%d/%m/%Y'

class CalBoxWidget(BasicDateBox):
    
    def __init__(self, attrs=None):
        super(CalBoxWidget, self).__init__(attrs)
        
        self.attrs['data-options'] = u'{"mode": "calbox", "calUsePickers": true, "overrideDateFormat": "%d/%m/%Y", "calNoHeader": true}'

class DateBoxWidget(BasicDateBox):
    
    def __init__(self, attrs=None):
        super(DateBoxWidget, self).__init__(attrs)
        
        self.attrs['data-options'] = u'{"mode": "datebox", "overrideDateFormat": "%d/%m/%Y"}'

class SlideBoxWidget(BasicDateBox):
    
    input_type = 'date'
    
    def __init__(self, attrs=None):
        super(SlideBoxWidget, self).__init__(attrs)
        
        self.attrs['data-options'] = u'{"mode": "slidebox", "overrideDateFormat": "%d/%m/%Y"}'

class BasicDateTimeBox(forms.DateTimeInput):
    
    input_type = 'datetime'
    
    def __init__(self, attrs=None):
        super(BasicDateTimeBox, self).__init__(attrs)
        if attrs is not None:
            self.attrs = attrs.copy()
        
        self.attrs['data-role'] = 'datebox'
        
        if not 'format' in self.attrs:
            self.attrs['format'] = '%d/%m/%Y %H:%M'

class SlideTimeBoxWidget(BasicDateTimeBox):
    
    def __init__(self, attrs=None):
        super(SlideTimeBoxWidget, self).__init__(attrs)
        
        self.attrs['data-options'] = u'{"mode": "slidebox", "overrideDateFormat": "%d/%m/%Y %H:%M", "overrideSlideFieldOrder":["y","m","d","h","i"]}'

class JQMSelectMultiple(forms.SelectMultiple):
    
    def __init__(self, attrs=None):
        
        super(JQMSelectMultiple, self).__init__(attrs)
        
        self.attrs['data-native-menu'] = 'false'


class JQMSelect(forms.Select):
    
    def __init__(self, attrs=None):
        
        super(JQMSelect, self).__init__(attrs)
        
        self.attrs['data-native-menu'] = 'false'
