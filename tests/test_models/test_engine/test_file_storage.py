#!/usr/bin/python3
""" TEST BASE MODEL"""

import unittest
import models
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
class test_file_storage(unittest.TestCase):
    def testFile(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testObj(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def testAll(self):
        dictionary = storage.all()
        self.assertEqual(type(dictionary), dict)

    def testNew(self):
        new = storage.all().copy()
        storage.new(BaseModel())
        self.assertNotEqual(new, storage.all())

    def test_reload(self):
        st = FileStorage()
        st.all().clear()
        st.reload()
        self.assertTrue(len(st.all()) > 0)

   

if __name__ == '__main__':
    unittest.main()
