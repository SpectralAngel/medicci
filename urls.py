# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import IndexView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^contactos/', include('medicci.contactos.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	
	url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        dict(
            template_name = 'jqm/login.html',
        ),
        name='login'),
    
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        dict(
            template_name = 'jqm/logout.html',
        ),
        name='logout'),
)
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
