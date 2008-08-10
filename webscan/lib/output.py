from django.http import HttpResponse
import simplejson

def json(method):
    return lambda *args: HttpResponse(simplejson.dumps(method(*args)))

