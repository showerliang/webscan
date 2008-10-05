from django.views.static import serve
from django.http import HttpResponseForbidden, HttpResponseNotFound

from webscan.server.django.utils import json, send_file, login_required
from webscan.lib.core.user import User

@login_required
@json
def list_image_groups(request, username):
    user = User(username)
    return user.list_image_groups()
    
@login_required
@json
def list_images(request, username, group):
    user = User(username)
    return user.list_images(group)
    
@login_required
def get_image(request, username, group, image_name):
    user = User(username)
    image_path = user.get_image(group, image_name)
    if image_path:
        return send_file(request, image_path)
    else:
        return HttpResponseNotFound()
        
