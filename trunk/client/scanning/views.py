import os

from django.http import HttpResponseNotFound
from django.core.urlresolvers import reverse
import pyscanning as scanners
import simplejson

from daemon.scanning.lib.user import User
from daemon.utils import json, send_file

@json
def list_scanners(request):
    return scanners.list()

@json
def get_scanner_info(request, id):
    return scanners.get(id).info()

@json
def scan_page(request, id, docname, pagename):
    scanner = scanners.get(id)
    image = scanner.scan()
    user = User()
    doc = user.getdocument(docname)        
    if doc is None:
        user.createdocument(docname)
        doc = user.getdocument(docname)        
    doc.addpage(pagename, image)

    host = 'http://'+request.get_host()
    host_image = reverse('get-page',args=(user.username, docname, pagename))+".png"
    return host + host_image

def get_page(request, username, docname, pagename):
    user = User(username)
    doc = user.getdocument(docname)
    pagename_without_ext = os.path.splitext(pagename)[0]
    pagepath = doc.pages[pagename_without_ext].viewpath

    if os.path.exists(pagepath):
        return send_file(request, pagepath)
    else:
        return HttpResponseNotFound()

def get_page_thumb(request, username, docname, pagename):
    user = User(username)
    doc = user.getdocument(docname)
    pagename_without_ext = os.path.splitext(pagename)[0]
    pagepath = doc.pages[pagename_without_ext].thumbpath

    if os.path.exists(pagepath):
        return send_file(request, pagepath)
    else:
        return HttpResponseNotFound()

@json
def list_documents(request, username):
    user = User(username)
    docs = user.documents
    return [ docs[key].name for key in docs ]

@json
def list_doc_pages(request, username, docname):
    user = User(username)
    doc = user.getdocument(docname)
    pages = doc.pages
    return [ pages[key].info() for key in pages ]

@json
def get_pdf_document(request, username, docname):
    user = User(username)
    
    docname_without_ext = os.path.splitext(docname)[0]
    doc = user.getdocument(docname_without_ext)

    if doc is not None:
        pages = simplejson.loads(request.GET.get('pages'))
        doctitle = request.GET.get('doctitle')
        lang = request.GET.get('lang')

        docpath = doc.topdf(doctitle, pages, lang)

        if os.path.exists(docpath):
            return docpath

    return HttpResponseNotFound()

@json
def get_user(request):
    return User().todict()
