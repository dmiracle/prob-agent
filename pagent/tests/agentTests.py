import unittest
import sys
import os

sys.path.append(os.path.dirname(__file__))

from pagent.agent import Agent
class TestAgent(unittest.TestCase):
    
    test_agent = Agent()

    def test_constructor(self):
        self.assertTrue(self.test_agent.name)
        self.assertTrue(self.test_agent.uid)

    def test_init_props(self):
        self.test_agent.init_props()
        self.assertTrue(self.test_agent.props)

if __name__ == '__main__':
    unittest.main()