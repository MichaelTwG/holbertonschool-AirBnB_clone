#!/usr/bin/python3
""" TEST BASE MODEL"""

import unittest
from models.base_model import BaseModel
import models

class test_file_storage(unittest.TestCase):
    def testFile(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testObj(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def testAll(self):
        dictionary = models.storage.all()
        self.assertEqual(type(dictionary), dict)

    def testNew(self):
        new = models.storage.all().copy()
        models.storage.new(BaseModel())
        self.assertNotEqual(new, models.storage.all())

    def test_reload(self):
        models.storage.__file_path = "NON_EXIST_FILE"
        self.assertRaises(FileNotFoundError, models.storage.reload())

if __name__ == '__main__':
    unittest.main()