from webscan.lib.core.driver_wrapper import BaseScannerWrapper, BaseScannerCollectionWrapper
import sane

class ScannerCollection(BaseScannerCollectionWrapper):
    def __init__(self):
        pass
 
    def __refresh__(self):
        for scanner in self:
            self.pop(0)
            scanner.__close__()
        sane.exit()


        sane.init()
        devices = sane.get_devices()    
        for dev in devices: 
            id = len(self)
            try:
                scanner = Scanner(id, dev[0], dev[1], dev[2], dev[3])
                self.append(scanner)
            except:
                pass
    
    def get(self, scanner_id):
        id = int(scanner_id)
        self.__refresh__()
        for dev in self:    
            if dev.id == id:
                return dev
        return None

    def list(self):
        self.__refresh__()
        return tuple([str(scanner) for scanner in self])

class Scanner(BaseScannerWrapper):  
    def __init__(self, id, device, manufacturer, name, description):
        self.id = id
        self.manufacturer = manufacturer
        self.name = name
        self.description = description
        self.__scanner__ = sane.open(device)

    def __str__(self):
        return '%s- %s: %s' % (self.id, self.manufacturer, self.name) 
    
    def scan(self):
        return self.__scanner__.scan()
    
    def info(self):
        return self.id, self.manufacturer, self.name, self.description
   
    def __close__(self):
        self.__scanner__.close()
    # TODO:     
    #def status(self):
    #    pass
