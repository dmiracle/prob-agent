from pagent.agent import Agent
from pagent.population import Population
from pagent.distribution import Distribution

def run():
    print("Running . . .")
    population = Population()
    population.init_population(25, True)
    disty = Distribution()