from webscan import settings

try:
    # TODO: Change to __import__ 
    exec("from webscan.drivers.%s import ScannerCollection" % settings.DRIVER_WRAPPER)
    __scanners__ = ScannerCollection()
    del ScannerCollection
except ImportError:
    pass
    #TODO: Log error


def list():
    return __scanners__

def get(id):
    return __scanners__.get(id)

