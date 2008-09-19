from webscan.core.action import BaseAction

class PDF(BaseAction):

    def run(self, pipeline):
        print pipeline.actions['ocr'].image_text
