import random as rnd
import itertools as it
import funkybob
import uuid

def rollForValue(k):
    distributions = {
        'sex': (1, ['M', 'F']),
        'pregnant': ([.1, .9], [True, False])
    }
    
    dist = distributions[k]

    if dist[0] == 1:
        return rnd.choice(dist[1])
    elif len(dist[0]) == len(dist[1]):
        bigN = sum(dist[0])
        randRoll = rnd.random()
        running_total = 0 
        for top, res in zip(dist[0], dist[1]):
            running_total += top
            if randRoll < running_total:
                return res
    else:
        return Exception

class Agent:
    props = {}
    
    def __init__(self):
        self.uid = uuid.uuid4()
        namer = funkybob.RandomNameGenerator()
        it = iter(namer)
        self.name = next(it)

    def prop_roll(self, k):
        try:
            v = rollForValue(k)
            return v
        except KeyError as e:
            print('Key Error, no dist with name ', k, ' ', str(e))
        except Exception as e:
            print(repr(e))

    def add_prop(self, k):
        if k in self.props.keys():
            return "Key already exists, use recheck_prop to roll again"
        self.props[k] = self.prop_roll(k)
        print("Add prop done")

    def recheck_prop(self, k):
        if k not in self.props.keys():
            return "Key does not exist, use add_prop to create"
        self.props[k] = self.prop_roll(k)
        print("Recheck prop done")
