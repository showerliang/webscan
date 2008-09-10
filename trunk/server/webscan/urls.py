from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^services/', include('webscan.services.urls')),
)
