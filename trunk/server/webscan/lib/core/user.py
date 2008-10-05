import os 
from os.path import exists
from webscan.lib.conf import settings
from webscan.lib.core import scanners

class User(object):
    def __init__(self, username):
        self.username = username
        self.__userspace_path__ = '%s/%s' % (settings.USER_SPACE, username)
        if not exists(self.__userspace_path__):
            os.makedirs(self.__userspace_path__)
            os.makedirs(self.__userspace_path__+'/default/')

    def scan(self, scanner_id, image_name, image_group=None):

        if image_group:
            group_path = '%s/%s' % (self.__userspace_path__, image_group)
            if not exists(group_path):
                os.makedirs(group_path)
            image_path = '%s/%s.tif' % (group_path, image_name)
        else:
            image_path = '%s/default/%s.tif' % (self.__userspace_path__, image_name)

        image_path = os.path.normpath(image_path)
        if exists(image_path):
            raise Exception('Image already exists. Choose another name')
        
        image = scanners.get(scanner_id).scan()
        image.save(image_path)
        return True

    def list_image_groups(self):
        return os.listdir(self.__userspace_path__)

    def list_images(self, group='default'):
        return os.listdir(self.__userspace_path__ + '/' + group)
    
    def get_image(self, group, image_name):
        image_path = '%s/%s/%s' % (self.__userspace_path__, group, image_name)
        if exists(image_path):
            return os.path.normpath(image_path)
        return None

    
