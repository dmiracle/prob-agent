import random
import itertools as it
import funkybob
import uuid
import yaml
from pagent.distribution import Distribution

class Agent:
    
    def __init__(self):
        self.props = {}
        self.uid = uuid.uuid4()
        namer = funkybob.RandomNameGenerator()
        it = iter(namer)
        self.name = next(it)
        self.dist = Distribution()
    
    def init_props(self):
        self.props = self.dist.rollAll()


    def set_prop(self, k, v):
        self.props[k] = v


