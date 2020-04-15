import unittest
import time
from pagent import agent, population, distribution


class TestPopulation(unittest.TestCase):
    start_time = time.time()
    test_population = population.Population()
    test_population.init_population(100)
    print("Populated in %s ms" % int((time.time() - start_time) * 1000))

    def test_population_list(self): 
        self.assertTrue(self.test_population.population)

    def test_slice_pop(self):
        l = self.test_population.slice_pop('name')
        print(len(set(l)))
        self.assertTrue(l)
        l = self.test_population.slice_pop('uid')
        print(len(set(l)))
        self.assertTrue(l)

if __name__ == '__main__':
    unittest.main()