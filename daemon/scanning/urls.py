from django.conf.urls.defaults import *

urlpatterns = patterns('daemon.scanning',
    url(r'^user/$', 'views.get_user', name='get-user'),
    
    url(r'^scanner/$', 'views.list_scanners', name='list-scanners'),
    url(r'^scanner/(\d+)/$', 'views.get_scanner_info', name='get-scanner-info'),
    url(r'^scanner/(\d+)/scan/(\w+)/(\w+)/$', 'views.scan_page', name='scan-page'),
    
    url(r'^(\w+)/$', 'views.list_documents', name='list-documents'),
    url(r'^(\w+)/(\w+)/$', 'views.list_doc_pages', name='list-doc-pages'),

    # Using .* instead of \w+ because of the . in the img or doc name
    url(r'^(\w+)/(\w+)/view/(.*)$', 'views.get_page', name='get-page'), 
    url(r'^(\w+)/(\w+)/thumb/(.*)$', 'views.get_page_thumb', name='get-page-thumb'), 
    url(r'^(\w+)/download/(.*)$', 'views.get_pdf_document', name='get-pdf-document'), 
)

