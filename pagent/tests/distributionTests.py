import unittest
from pagent.distribution import Distribution

class TestDistribution(unittest.TestCase):
    test_distribuition = Distribution()

    def test_distribuition_map(self):
        self.assertTrue(self.test_distribuition.distributions)

    def test_rollForValue(self):
        for key, dist in self.test_distribuition.distributions.items():
            print({key : dist})
            roll = self.test_distribuition.rollForValue(dist)
            print(roll)
            self.assertTrue(roll)

if __name__ == '__main__':
    unittest.main()