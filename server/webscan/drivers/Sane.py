from webscan.core.driver_wrapper import BaseScannerWrapper, BaseScannerCollectionWrapper
import sane

class ScannerCollection(BaseScannerCollectionWrapper):
    def __init__(self):
        sane.init()
        devices = sane.get_devices()
        
        for dev in devices: 
            id = len(self)
            try:
                scanner = Scanner(id, dev[0], dev[1], dev[2], dev[3])
                self.append(scanner)
            except:
                pass
    
    def get(self, id):
        for dev in self:    
            if dev.id == id:
                return dev
        return None
       

class Scanner(BaseScannerWrapper):  
    def __init__(self, id, device, manufacturer, name, description):
        self.id = id
        self.manufacturer = manufacturer
        self.name = name
        self.description = description
        self.__scanner__ = sane.open(device)
       
    def scan(self):
        return self.__scanner__.scan()
    
    def info(self):
        return self.id, self.manufacturer, self.name, self.description
    
    # TODO:     
    #def status(self):
    #    pass
