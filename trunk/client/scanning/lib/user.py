import os
from daemon.scanning.lib.document import Document

class User(object):
    def __init__(self, username=None):
        if username is None:
            self.username = os.getenv('USERNAME')
            if not self.username:
                self.username = os.getenv('USER')
        else:    
            self.username = username

        # The following attriutes depends on each os:
        #   self.home
        #   self.appdir

        # Posix (Linux, Unix, etc...)
        if os.name == 'posix':
            self.home = os.getenv('HOME')
            self.appdir = self.home + '/' + ".webscan"

        # Windows
        elif os.name == 'nt':
            self.home = os.getenv('APPDATA')
            self.appdir = self.home + '/' + "webscan"
        
        # Not supported OS
        else:
            raise Exception('OS not supported')
        
        self.docdir = self.appdir + '/' + "documents"
        self.__createappdir()
        
        self.documents = {}
        self.__getdocuments()
        
    def __getdocuments(self):
        docnames = os.listdir(self.docdir)
        for docname in docnames:
            self.createdocument(docname)

    def __createappdir(self):
        """Creates the webscan directory if it don't exists."""   
        if not os.path.exists(self.appdir):
            os.mkdir(self.appdir)

        if not os.path.exists(self.docdir):
            os.mkdir(self.docdir)
    
    def createdocument(self, docname):
        doc = Document(docname, self)
        self.documents.update({doc.name:doc})
    
    def getdocument(self, docname):
        return self.documents.get(docname)
        
    def todict(self):
        return {"username": self.username, "docdir": self.docdir}
