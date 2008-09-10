from webscan import settings

try:
    exec("from webscan.drivers.%s import Scanner" % settings.DRIVER_WRAPPER)
except ImportError:
    pass
    #TODO: Log error

__all__ = ["Scanner"]
