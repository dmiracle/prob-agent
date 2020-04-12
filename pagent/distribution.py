import random
import yaml
import numpy
from scipy.interpolate import interp1d
from math import floor

class Distribution:

    distributions = {
        'sex': [1, ['M', 'F']],
        'pregnant': [[.15, .85], [True, False]],
        'normal': ["normal", 0, 0.2],
        'age' : ["interpolate", [(0, 1), (100, 0)]] 
    }

    distribution_arrays = {}

    def __init__(self, dist_file = "distributions.yml"):
        self.fname = dist_file

    def rollAll(self):
        props = {}
        for k, v in self.distributions.items():
            props.update({k : self.rollForValue(v)})
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
        elif dist[0] == "interpolate":
            return self.interpolate_dist(dist[1])
        elif dist[0] == 1:
            return random.choice(dist[1])
        elif len(dist[0]) == len(dist[1]):
            randRoll = random.random()
            running_total = 0 
            for top, res in zip(dist[0], dist[1]):
                running_total += top
                if randRoll < running_total:
                    return res, randRoll
        else:
            return Exception
    
    def fiftyfifty(self):
        return random.choice([True, False])

    def interpolate_dist(self, points):
        try:
            p = self.distribution_arrays[tuple(points)]
        except KeyError: 
            start = points[0]
            stop = points[-1]
            numpy.linspace(start[0], stop[0], 1000)
            x, y = list(zip(*points))
            f = interp1d(x, y, fill_value="extrapolate")
            xx = numpy.linspace(0, 100, 1000, endpoint=True)
            p = []
            a = .01
            m = sum(xx)/len(xx)
            for xxx in xx:
                xxx = xxx + (random.random() * m/100)
                i = floor(f(xxx)/a)
                for j in range(i):
                    p.append(xxx)
            self.distribution_arrays.update( {tuple(points) : p})
        return random.choice(p)