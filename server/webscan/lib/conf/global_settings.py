# Default Django settings. Override these with settings in the module
# pointed-to by the WEBSCAN_SETTINGS_MODULE environment variable.

DRIVER_WRAPPER = 'Sane'

ACTIONS = (
    ('pdf', 'webscan.actions.pdf.PDF'),
    ('ocr', 'webscan.actions.ocr.OCR'),
)

USER_SPACE = 'userspace/'

