import Image

from webscan.core.action import BaseAction
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class PDF(BaseAction):

    def run(self, pipeline):
        # TODO: Implement variable name for the document 
        self.doc_path = pipeline.userspace + pipeline.doc_name
        c = canvas.Canvas(self.doc_path, pagesize=letter)
        width, height = letter
        
        try:
            image_text = pipeline.actions['ocr'].image_text 
            y = height
            for line in image_text.split('\n'):
                c.drawString(10, y, line)
                y -= 15
        except KeyError:
            # If OCR not used gen pdf without text
            pass
       
        c.drawImage(pipeline.image_path, 0, 0, width, height)
        c.showPage()
        c.save()
