from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from webscan.server.django.utils import json
from webscan.lib.core import scanners
from webscan.lib.core.user import User

@login_required
@json
def list(request):
    return scanners.list()

@login_required
@json
def get(request, id):
    return str(scanners.get(id))

@login_required
@json
def scan(request, scanner_id):
    try:
        image_name = request.GET['img_name']
    except Exception, e:
        raise Exception("The GET argument 'img_name' is mandatory")

    user = User(request.user.username)
    
    try:
        image_group = request.GET['img_group']
    except:
        image_group = 'default' 
    
    ok = user.scan(scanner_id, image_name, image_group)
    if ok:
        host = 'http://'+request.get_host()
        host_image = reverse('get-image',args=(user.username, image_group, image_name))+'.tif'
        return host + host_image
    else:
        return None
