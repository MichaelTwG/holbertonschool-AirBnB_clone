#!/usr/bin/python3
""" TEST BASE MODEL"""

import unittest
from models.base_model import BaseModel

class test_base_models(unittest.TestCase):
    
    def test_normal_case(self):
        base = BaseModel()
        self.assertIsNotNone(base.id)
        self.assertIsNotNone(base.created_at)
        self.assertEqual(base.created_at, base.updated_at)
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)
        self.assertTrue(isinstance(base.to_dict(), dict))
        
if __name__ == '__main__':
    unittest.main()