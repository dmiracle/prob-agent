import unittest
import agent
import distribution
import population

class TestAgent(unittest.TestCase):
    
    test_agent = agent.Agent()

    def test_constructor(self):
        self.assertTrue(self.test_agent.name)
        self.assertTrue(self.test_agent.uid)

class TestPopulation(unittest.TestCase):
    test_population = population.Population()

    def test_population_list(self):
        self.assertTrue(self.test_population.population == [])

class TestDistribution(unittest.TestCase):
    test_distribuition = distribution.Distribution()

    def test_distribuition_map(self):
        self.assertTrue(self.test_distribuition.distributions)

if __name__ == '__main__':
    unittest.main()