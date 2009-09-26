from django.views.static import serve
from django.views.generic.simple import redirect_to
from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.core.urlresolvers import reverse
from webscan.server.django.utils import json, send_file, login_required
from webscan.lib.core.user import User

@login_required
@json
def list_image_groups(request, username):
    user = User(username)
    return user.list_image_groups()

@json
def info(request):
    if request.user.is_authenticated(): 
        auth = True
        username = request.user.username
    else:
        auth = False
        username = None
    
    return {'username': username, 'auth': auth}
    
    
@login_required
@json
def list_images(request, username, image_group):
    user = User(username)
    return user.list_images(image_group)
    
@login_required
def get_image(request, username, image_group, image_name):
    user = User(username)
    image_path = user.get_image(image_group, image_name)
    if image_path:
        return send_file(request, image_path)
    else:
        return HttpResponseNotFound()
        
