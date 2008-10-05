
import os

if os.name == 'posix':
    from webscan.lib.contrib.wrapper.Sane import ScannerCollection
elif os.name == 'nt':
    from webscan.lib.contrib.wrapper.Twain import ScannerCollection
else:
    #TODO: Log error
    raise Exception('OS not supported')

__scanners__ = ScannerCollection()
del ScannerCollection


def list():
    return __scanners__.list()

def get(id):
    return __scanners__.get(id)
