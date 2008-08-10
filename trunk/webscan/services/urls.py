from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Scanner
    url (r'^scanner/$', 'webscan.services.views.scanner.list'),
    url (r'^scanner/add/$', 'webscan.services.views.scanner.add'),
    url (r'^scanner/(.*)/$', 'webscan.services.views.scanner.view'),
    url (r'^scanner/(.*)/modify/$', 'webscan.services.views.scanner.update'),
    url (r'^scanner/(.*)/delete/$', 'webscan.services.views.scanner.delete'),
    url (r'^scanner/(.*)/status/$', 'webscan.services.views.scanner.status'),
    url (r'^scanner/(.*)/scan/$',   'webscan.services.views.scanner.scan'),
    
    # User
    url (r'^user/$', 'webscan.services.views.user.list'),
    url (r'^user/add$/', 'webscan.services.views.user.add'),
    url (r'^user/(.*)/$', 'webscan.services.views.user.view'),
    url (r'^user/(.*)/modify/$', 'webscan.services.views.user.modify'),
    url (r'^user/(.*)/delete/$', 'webscan.services.views.user.delete'),

    url (r'^user/(.*)/page/$', 'webscan.services.views.page.list'),
    url (r'^user/(.*)/page/(.*)/$', 'webscan.services.views.page.view'),
    url (r'^user/(.*)/page/(.*)/delete/$', 'webscan.services.views.page.delete'),

    url (r'^user/(.*)/document/$', 'webscan.services.views.document.list'),
    url (r'^user/(.*)/document/new$', 'webscan.services.views.document.new'),
    url (r'^user/(.*)/document/(.*)/$', 'webscan.services.views.document.download'),
    url (r'^user/(.*)/document/(.*)/delete/$', 'webscan.services.views.document.delete'),
    
    # Auth
    url (r'^auth/$', 'webscan.services.views.auth.info'),
    url (r'^auth/login/$', 'webscan.services.views.auth.login'),
    url (r'^auth/logout/$', 'webscan.services.views.auth.logout'),
)
