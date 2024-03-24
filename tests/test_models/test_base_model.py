#!/usr/bin/python3
"""Module contains unittest for 'base_model.py' module"""


import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)

    def test_save(self):
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)

    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_str(self):
        obj = BaseModel()
        self.assertIsInstance(str(obj), str)


if __name__ == '__main__':
    unittest.main()
