import random
import itertools as it
import funkybob
import uuid
import yaml

distributions = {
    'sex': [1, ['M', 'F']],
    'pregnant': [[.15, .85], [True, False]]
}

class Agent:
    
    def __init__(self, dist_file = "./distributions.yml"):
        self.props = {}
        self.uid = uuid.uuid4()
        namer = funkybob.RandomNameGenerator()
        it = iter(namer)
        self.name = next(it)
        # random.seed()

    def import_yaml(self, fname):
        with open(fname) as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        return data

    def export_yaml(self, data, fname):
        with open(fname, 'w') as file:
            data_file = yaml.dump(data, file)
        return data_file

    def rollForValue(self, k, dist):
        # dist = distributions[k]
        # dist ~ [[a, . . . ], [b, . . . .]]
        # dist[0] is either:
        #   1 -- choose uniform
        #   [a1, a2, . . .] prob of [b1, b2, . . .]
        #  
        if dist[0] == 1:
            return random.choice(dist[1])
        elif len(dist[0]) == len(dist[1]):
            randRoll = random.random()
            running_total = 0 
            for top, res in zip(dist[0], dist[1]):
                # print(randRoll, top, res)
                running_total += top
                if randRoll < running_total:
                    return res, randRoll
        else:
            return Exception

    def prop_roll(self, k, dist):
        try:
            v, roll = self.rollForValue(k, dist)
            return v, roll
        except KeyError as e:
            print('Key Error, no dist with name ', k, ' ', str(e))
        except Exception as e:
            print(repr(e))

    def set_prop(self, k, v):
        self.props[k] = v

    def add_prop(self, k, dist):
        if k in self.props.keys():
            return "Key already exists, use recheck_prop to roll again"
        else:
            self.props[k], roll = self.prop_roll(k, dist)
            return self.props[k], roll


    def recheck_prop(self, k, dist):
        if k not in self.props.keys():
            return "Key does not exist, use add_prop to create"
        else:
            self.props[k], roll = self.prop_roll(k, dist)
            return self.props[k], roll

