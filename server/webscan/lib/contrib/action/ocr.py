import Image
import subprocess
import os
import random

from datetime import datetime
from webscan.core.action import BaseAction

TESSERACT_BIN = '/usr/bin/tesseract' # Name of executable to be called at command line

def randstr(lenght=8, charset='abcdefghijklmnopqrstuvxywz0123456789'):
    """Generates a random string"""

    password = []
    for i in range(lenght):
        rand = random.randint(0,len(charset)-1)
        password.append(charset[rand])

    return "-" + "".join(password)

def call_tesseract(scratch_image, output):
    """Calls external tesseract on input file (restrictions on types),
    outputting output+'txt'"""
    
    args = [TESSERACT_BIN, scratch_image, output]
    proc = subprocess.Popen(args)
    retcode = proc.wait()

def image_to_string(image, cleanup = True):
    """Converts im to file, applies tesseract, and fetches resulting text.
    If cleanup=True, delete scratch files after operation."""
    
    current_sec = datetime.today().strftime("%s")
    rand = randstr(8)
    scratch_image = '/tmp/' + current_sec + rand + ".tif"
    output = '/tmp/' + rand + current_sec
    
    try:
        image_to_scratch(image, scratch_image)
        call_tesseract(scratch_image, output)
        fp = open(output+'.txt')
        txt = fp.read()
        fp.close()
    finally:
        if cleanup:
            perform_cleanup(scratch_image, output)
    return txt

def image_to_scratch(image, scratch_image):
    """Saves image in memory to scratch file. '.tif' format will be read correctly by Tesseract"""
    im = Image.open(image).convert('L')
    im.save(scratch_image, dpi=(200,200), compression=None)

def perform_cleanup(scratch_image, output):
    """Clean up temporary files from disk"""
    for name in (scratch_image, output+'.txt'):
        try:
            os.remove(name)
        except OSError:
            pass

class OCR(BaseAction):

    def run(self, pipeline):
        self.image_text = image_to_string(pipeline.image_path)
