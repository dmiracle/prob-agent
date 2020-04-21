from pagent.agent import Agent

class Population:
    ''' 
    Population is a list of agents found at Population.population
    '''

    def __init__(self):
        self.population = []

    def get_population(self):
        return self.population

    def init_population(self, size, printing=False, roll=True):
        self.population = []
        for i in range(size):
            x = Agent()
            if roll:
                x.init_props()
            if printing:
                print(i, ": ", x.name, x.uid)
            self.population.append(x)

    def iterative_runout(self, key, val):
        # val is the target value, for runout from. 
        # Ex: True to False, specify False
        inc = 0 
        res = []
        while self.how_many(key, val) > 0:
            for a in self.population:
                if a.props[key] == val:
                    a.recheck_prop(key)
            res.append([inc, self.how_many(key, val)])
            inc += 1
        return res

    def how_many(self, key, value):
        return len([1 for a in self.population if a.props[key] == value ])

    def slice_pop(self, key):
        # Return N length list of each value for given key
        # list_of_values = slice_pop(key)
        l = []
        for a in self.population:
            l.append(a.as_dict()[key])
        return l

    def as_dict(self):
        d = {}
        p = []
        for a in self.population:
            p.append(a.as_dict())
        d['population'] = p
        return d