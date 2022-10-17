#!/usr/bin/python3
""" AMENITY TEST """
import unittest
from models.amenity import Amenity

class test_class_amenity(unittest.TestCase):
    """ Test amenity """

    def test_amenity(self):
        amenity_1 = Amenity()
        self.assertEqual(amenity_1.name, "")

if __name__ == '__main__':
    unittest.main()