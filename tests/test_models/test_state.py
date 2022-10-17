#!/usr/bin/python3
""" TEST STATE """
import unittest
from models.state import State

class test_class_state(unittest.TestCase):
    """ Test state """

    def test_state(self):
        state_1 = State()
        self.assertEqual(state_1.name, "")

if __name__ == '__main__':
    unittest.main()