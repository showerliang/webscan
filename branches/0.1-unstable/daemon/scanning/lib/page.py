import os
import Image

class Page(object):
    def __init__(self, name, document, image=None):

        self.name = name
        self.path = "%s/%s.tiff" % (document.rawpath, name)     
        self.thumbpath = "%s/%s.png" % (document.thumbpath, name)
        self.viewpath = "%s/%s.png" % (document.viewpath, name)

        if os.path.exists(self.path):
            # Page already exists and is trying to save using same name
            if image is not None:
                raise OSError(17, 'Page exists. Choose other name')
            # Page already exists and is just getting info
            else:
                self.image = Image.open(self.path)
        else:
            # Page doesn't exists. Save it! 
            if image is not None:
                # Image is not instance of Image.Image (PIL)
                if not isinstance(image, Image.Image):
                    raise TypeError('Page was expected to be instance of Image.Image')
                else:
                    # Size based on 200dpi and paper letter
                    image = image.crop((0, 0, 1600, 2300))
                    self.image = image
                    image.save(self.path) 
                    image.save(self.viewpath) 
                    image.thumbnail((120,160)) 
                    image.save(self.thumbpath) 
            # Page doesn't exists and there is no image to create
            else:
                raise Exception("Page doesn't exists and no image was passed")
        
    def info(self):
        return {'name': self.name, 
                'viewpath': self.viewpath, 
                'thumbpath': self.thumbpath,
                'path': self.path,
                } 
 
