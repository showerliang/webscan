import os

from pilpe import Pipeline
from pilpe.plugins import OCR, PDF

from page import Page

class Document(object): 
    def __init__(self, name, user):
        self.name = name
        self.path = "%s/%s" % (user.docdir, name)
        self.rawpath = "%s/%s/raw" % (user.docdir, name)
        self.viewpath = "%s/%s/view" % (user.docdir, name)
        self.thumbpath = "%s/%s/thumb" % (user.docdir, name)
    
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            os.mkdir(self.rawpath)
            os.mkdir(self.viewpath)
            os.mkdir(self.thumbpath)
        
        self.pages = {}
        self.__getpages()
    
    def addpage(self, pagename, image):
        page = Page(pagename, self, image)
        self.pages.update({page.name:page})
   
    def getpage(self, pagename):
        return Page(pagename, self)
        
    def __getpages(self):
        pagenames = os.listdir(self.rawpath)
        for pagename in pagenames:
            pagename = os.path.splitext(pagename)[0]
            page = self.getpage(pagename)
            self.pages.update({page.name:page})

    def topdf(self, doctitle, pagenames, lang=None):
        images_path = [ "%s/%s.tiff" % (self.rawpath, pagename) for pagename in pagenames ]

        config = {}
        if lang:
            config['lang'] = lang

        ocr = OCR(config)

        pdfpath = "%s/%s.pdf" % (self.path, self.name)
        pdf = PDF({
            'path': pdfpath, 
            'title': doctitle,
        })

        pipeline = Pipeline()
        pipeline.register(ocr)
        pipeline.register(pdf)
        pipeline.run(images_path)
      
        return pdfpath 
    
