import random
import yaml


class Distribution:

    distributions = {
        'sex': [1, ['M', 'F']],
        'pregnant': [[.15, .85], [True, False]],
        'normal': ["normal", 0, 0.2]
    }

    def __init__(self, dist_file = "distributions.yml"):
        self.fname = dist_file

    def rollAll(self):
        props = {}
        for k in self.distributions:
            props.update({k : self.rollForValue(k)})
        return props

    def import_yaml(self, fname):
        with open(fname) as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        return data

    def export_yaml(self, data, fname):
        with open(fname, 'w') as file:
            data_file = yaml.dump(data, file)
        return data_file

    def rollForValue(self, dist):
        # dist = distributions[k]
        # dist ~ [[a, . . . ], [b, . . . .]]
        # dist[0] is either:
        #   1 -- choose uniform
        #   [a1, a2, . . .] prob of [b1, b2, . . .]
        #  
        if dist[0] == "normal":
            return random.normalvariate(dist[1], dist[2])
        elif dist[0] == 1:
            return random.choice(dist[1])
        elif len(dist[0]) == len(dist[1]):
            randRoll = random.random()
            running_total = 0 
            for top, res in zip(dist[0], dist[1]):
                print(top, res)
                running_total += top
                if randRoll < running_total:
                    return res, randRoll
        else:
            return Exception
    
    def fiftyfifty(self):
        return random.choice([True, False])