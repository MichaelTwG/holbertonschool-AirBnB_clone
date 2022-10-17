#!/usr/bin/python3
""" TEST CITY """

import unittest
from models.city import City

class test_class_city(unittest.TestCase):

    def test_city(self):
        city_1 = City()
        self.assertEqual(city_1.state_id, "")

        self.assertEqual(city_1.name, "")

if __name__ == '__main__':
    unittest.main()
