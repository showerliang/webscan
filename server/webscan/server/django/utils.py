import simplejson
import os
from django.http import HttpResponse, HttpResponseForbidden
from django.core.servers.basehttp import FileWrapper
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required as django_login_required

def json(view):
    def decorator(*args):
        response = view(*args)
        try:
            response = simplejson.dumps(response)
        except:
            pass
        
        if isinstance(response, HttpResponse):
            return response
        else:
            return HttpResponse(response)

    return decorator
    

def send_file(request, filename):
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type='image/tif')
    response['Content-Length'] = os.path.getsize(filename)
    return response

def login_required(view):
    def decorator(request, username=None, *args):
        if not username:
            username = request.user.username
        else:
            try:
                User.objects.get(username=username)
            except:
                raise Exception("User '%s' doesn't exists" % username)

            if not request.user.is_superuser and username != request.user.username:
                return HttpResponseForbidden()

        return view(request, username, *args)
    return django_login_required(decorator)
