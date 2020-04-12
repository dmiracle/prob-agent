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
        namer = funkybob.RandomNameGenerator(separator=' ')
        it = iter(namer)
        self.name = next(it).title()
        self.dist = Distribution()
    
    def init_props(self):
        self.props = self.dist.rollAll(self.dist.distributions)


    def set_prop(self, k, v):
        self.props[k] = v

    def as_dict(self):
        d = self.props
        d['name'] = self.name
        d['uid'] = self.uid
        return d
