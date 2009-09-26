from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^', include('daemon.scanning.urls')),
)
