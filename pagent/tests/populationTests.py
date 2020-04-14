import unittest
from pagent import agent, population, distribution


class TestPopulation(unittest.TestCase):
    test_population = population.Population()
    test_population.init_population(25)

    def test_population_list(self): 
        self.assertTrue(self.test_population.population)

    def test_slice_pop(self):
        self.assertTrue(self.test_population.slice_pop)

if __name__ == '__main__':
    unittest.main()