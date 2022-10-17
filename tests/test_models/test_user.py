#!/usr/bin/python3
""" TEST USER """

import unittest
from models.user import User

class test_user(unittest.TestCase):

    def test_none_case(self):
        user_1 = User()
        self.assertEqual(user_1.email, "")

        self.assertEqual(user_1.password, "")

        self.assertEqual(user_1.first_name, "")

        self.assertEqual(user_1.last_name, "")

if __name__ == '__main__':
    unittest.main()
