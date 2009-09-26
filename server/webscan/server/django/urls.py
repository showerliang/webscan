from django.conf.urls.defaults import *

urlpatterns = patterns('webscan.server.django.views',
    url (r'^scanner/$', 'scanner.list',name='list-scanners'),
    url (r'^scanner/(\d+)/$', 'scanner.get', name='get-scanner'),
    url (r'^scanner/(\d+)/scan/$', 'scanner.scan', name='scanner-scan'),
    url (r'^user/$', 'user.info', name='user'),
    url (r'^user/(?P<username>\w+)/$', 'user.list_image_groups', name='list-image-groups'),
    url (r'^user/(?P<username>\w+)/(?P<image_group>\w+)/$', 'user.list_images', name='list-images'),
    url (r'^user/(?P<username>\w+)/(?P<image_group>\w+)/(?P<image_name>.*)$', 'user.get_image', name='get-image'), # Using .* instead of \w+ because of the . in the img name
)
