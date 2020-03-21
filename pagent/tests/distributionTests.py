import unittest
from pagent.distribution import Distribution

class TestDistribution(unittest.TestCase):
    test_distribuition = Distribution()

    def test_distribuition_map(self):
        self.assertTrue(self.test_distribuition.distributions)

if __name__ == '__main__':
    unittest.main()