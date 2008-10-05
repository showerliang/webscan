from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^webscan/', include('webscan.server.django.urls')),
    (r'^admin/(.*)', admin.site.root),
    url (r'^webscan/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    url (r'^webscan/logout/$', 'django.contrib.auth.views.logout'),
)
