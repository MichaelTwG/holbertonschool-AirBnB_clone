#!/usr/bin/python3
""" TEST REVIEW """

import unittest
from models.review import Review

class test_class_review(unittest.TestCase):

    def test_review(self):
        review_1 = Review()

        self.assertEqual(review_1.place_id, "")

        self.assertEqual(review_1.user_id, "")

        self.assertEqual(review_1.text, "")

if __name__ == '__main__':
    unittest.main()