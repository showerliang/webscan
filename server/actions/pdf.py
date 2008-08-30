from webscan.lib.action import BaseAction

class PDF(BaseAction):

    def run(self, pipeline_args):
        print pipeline_args.update(self.args)
