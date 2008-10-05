from django.conf.urls.defaults import *
from webscan.server.django import views
from webscan.lib.conf import settings

urlpatterns = patterns('',
    url (r'scanner/$', views.scanner.list, name='list-scanners'),
    url (r'scanner/(\d+)/$', views.scanner.get, name='get-scanner'),
    url (r'scanner/(\d+)/scan/$', views.scanner.scan, name='scanner-scan'),
    url (r'user/$', views.user.list_image_groups, name='user'),
    url (r'user/(\w+)/$', views.user.list_image_groups, name='list-image-groups'),
    url (r'user/(\w+)/(\w+)/$', views.user.list_images, name='list-images'),
    url (r'user/(\w+)/(\w+)/(.*)$', views.user.get_image, name='get-image'),
)

