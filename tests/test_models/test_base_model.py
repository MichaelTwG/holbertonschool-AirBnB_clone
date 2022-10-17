#!/usr/bin/python3
""" TEST BASE MODEL"""

import unittest
from models.base_model import BaseModel
import os

class test_base_models(unittest.TestCase):
    
    def test_normal_case(self):
        base = BaseModel()
        self.assertIsNotNone(base.id)
        self.assertIsNotNone(base.created_at)
        self.assertEqual(base.created_at, base.updated_at)
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)
    
    def test_to_dict(self):
        base2 = BaseModel()
        base_dict = base2.to_dict()
        self.assertEqual(type(base_dict), type({}))
        self.assertIsNotNone(base_dict["id"])
    
    def test_str(self):
        base = BaseModel()
        out = f"[{base.__class__.__name__}] ({base.id}) {base.__dict__}"
        _str = base.__str__()
        self.assertEqual(out, _str)

    def test_save(self):
        base2 = BaseModel()

        try:
            os.remove('file.json')
        except Exception:
            pass
        
        base2.save()
        self.assertTrue(os.path.exists('file.json'))
        
if __name__ == '__main__':
    unittest.main()
