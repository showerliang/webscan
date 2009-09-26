import simplejson
import os
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.core.servers.basehttp import FileWrapper
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required as django_login_required

#decorator_with_args = lambda decorator: lambda *args, **kwargs: lambda func: decorator(func, *args, **kwargs)
#@decorator_with_args

def json(view): 
    def decorator(request, *args, **kwargs):
        jsoncallback = request.GET.get('callback')
        if not jsoncallback:
            jsoncallback = view.__name__

        response = view(request, *args, **kwargs)
        try:
            JSONresponse = simplejson.dumps(response)
        except Exception, e:
            raise e     

        try:
            error_msg = response['error_msg']
            JSONresponse = "ajax.__error__("+JSONresponse+")"
        except:
            JSONresponse = jsoncallback+"("+JSONresponse+")"
            
        JSONresponse = "ajax.__complete__("+JSONresponse+")"
        return HttpResponse(JSONresponse)

    return decorator

def send_file(request, filename, content_type='image/tif'):
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type=content_type)
    response['Content-Length'] = os.path.getsize(filename)
    return response
    
def login_required(view):
    def decorator(request, *args, **kwargs):
        # If user is not logged in just use django login decorator
        if not request.user.is_authenticated():
            f = django_login_required(view)
            return f(request, *args, **kwargs)
        
        # If the decorated function don't receives username as arg
        #   there is no way to check if the user request is the 
        #   same user logged in
        username = kwargs.get('username')
        if not username:
            return view(request, *args, **kwargs)

        try:
            User.objects.get(username=username)
        except:
            raise Exception("User '%s' doesn't exists" % username)

        # The users can see only theirs own files except if is a superuser
        if not request.user.is_superuser and username != request.user.username:
            return HttpResponseForbidden()
        return view(request, *args, **kwargs)
    return decorator
