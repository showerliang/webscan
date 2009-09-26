import simplejson
import os.path
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper

def json(view): 
    def decorator(request, *args, **kwargs):
        response = view(request, *args, **kwargs)
        try:
            callback = request.REQUEST.get('callback')
            if not callback: callback = ''
            JSONresponse = "%s(%s)" % (callback, simplejson.dumps(response))
        except Exception, e:
            raise e     
        return HttpResponse(JSONresponse)

    return decorator

def send_file(request, filename, content_type='image/png'):
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type=content_type)
    response['Content-Length'] = os.path.getsize(filename)
    return response
