from webscan.core.action import BaseAction

class OCR(BaseAction):

    def run(self, pipeline_args):
        print pipeline_args.update(self.args)
