#!/usr/bin/python3
""" TEST BASE MODEL"""

import unittest
from models import user
from models.user import User

class test_user(unittest.TestCase):
    
    def test_none_case(self):
        user_1 = User()
        user_1.email = None
        self.assertEqual(user_1.email, None)

        user_1.password = None
        self.assertEqual(user_1.password, None)

        user_1.first_name = None
        self.assertEqual(user_1.first_name, None)

        user_1.last_name = None
        self.assertEqual(user_1.last_name, None)

    def test_normal_case(self):
        user_1 = User()
        user_1.email = "exeple@gmail.com"
        self.assertEqual(user_1.email, "exeple@gmail.com")

        user_1.password = "1234"
        self.assertEqual(user_1.password, "1234")

        user_1.first_name = "User_1"
        self.assertEqual(user_1.first_name, "User_1")

        user_1.last_name = "Unknow"
        self.assertEqual(user_1.last_name, "Unknow")

if __name__ == '__main__':
    unittest.main()
