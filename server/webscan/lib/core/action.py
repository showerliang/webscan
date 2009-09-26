from webscan.lib.conf import settings
from webscan.lib.type import odict

class Pipeline(object):
    def __init__(self, username, image):
        self.actions = odict()
        # Use username and image id to define the image_path
        # TODO:
        self.userspace = settings.USER_SPACE + '/' + username + '/'
        self.image_path = self.userspace + image

    def registerAction(self, action_name, action):
        self.actions[action_name] = action
        #TODO: Check if action is instance of a subclass of BaseAction if not raise exception and log

    def run(self):
        for action in self.actions:
            action.run(self)
         
    
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
        try:
            actionObj = Action(action['args'])
        except KeyError:
            actionObj = Action({})
        pipeline.registerAction(action['name'], actionObj)        
    return pipeline.run()

