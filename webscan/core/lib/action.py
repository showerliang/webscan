from webscan import settings


class Pipeline(object):
    def __init__(self, username, image):
        self.actions = []
        
        # Use username and image id to define the image_path
        image_path = ""
        self.args = {"image_path": image_path}
  
    def registerAction(self, action):
        self.actions.append(action)
        #TODO: Check if action is instance of a subclass of BaseAction if not raise exception and log

    def run(self):
        for action in self.actions:
            action.run(self.args)
        
        return self.args
         
    
class BaseAction(object):
    def __init__(self, args={}):
        self.args = args

    def run(self, pipeline_args):
        #TODO: Log and raise exception
        print "Not Implemented."


def import_action(action_name):
    try:
        action_path = dict(settings.ACTIONS)[action_name]
    except KeyError:
        raise Exception, '%s isn\'t a registered action.' % action_name
    
    try:
        dot = action_path.rindex('.')
    except ValueError:
        raise Exception, '%s isn\'t a action' % action_path
    ac_module, ac_classname = action_path[:dot], action_path[dot+1:]
    try:
        mod = __import__(ac_module,fromlist=[ac_classname])
        ac_class = getattr(mod, ac_classname)
        return ac_class
    except ImportError, e:
        raise Exception, 'Error importing action %s: "%s"' % (ac_module, e)
    

def run_actions(username, image, actionList):
    pipeline = Pipeline(username, image)

    for action in actionList:
        Action = import_action(action['name'])
        for i in dir(Action):
            print i, eval("Action."+i)
        actionObj = Action(action['args'])
        print issubclass(actionObj.__class__, BaseAction)
        pipeline.registerAction(actionObj)
        
    return pipeline.run()

