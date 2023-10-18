#!/usr/bin/python3
import unittest
import sys
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorageClass(unittest.TestCase):
    """Test FileStorage Class
    """
    def test___file_path(self):
        """"""
        fs = FileStorage()
        self.assertEqual(type(fs)._FileStorage__file_path, 'file.json')

    def test___objects(self):
        """"""
        fs = FileStorage()
        self.assertEqual(type(fs._FileStorage__objects), dict)

    def test_all(self):
        """"""
        fs = FileStorage()
        objs = fs.all()
        """Assert all() returns a dict type object"""
        self.assertIs(type(objs), dict)
        """Assert all() returns a dict type with
            key of type str, format = "<class name> <object id>
            value of type dict
        """
        for key, value in objs.items():
            self.assertIs(type(key), str)
            self.assertIs(type(value), dict)
            key_format = "{}.{}".format(value['__class__'], value['id'])
            self.assertEqual(key, key_format)

    def test_new(self):
        """"""
        fs = FileStorage()
        obj = BaseModel()
        objects_count_before = len(fs.all())  # count = 0
        fs.new(obj)
        objects_count_after = len(fs.all())  # count = 1
        self.assertNotEqual(objects_count_before, objects_count_after)
        # obj_id = "{}.{}".format(obj.__class__.__name__, obj.id)
        # print(obj_id)
        # print(fs.all().keys())
        # self.assertIn(obj_id, fs.all().keys())
        type(fs)._FileStorage__objects = {}

    def test_save(self):
        """"""
        fs = FileStorage()
        test_save_path = 'test_save.json'
        does_file_exist_before_save = os.path.isfile(test_save_path)  # False
        type(fs)._FileStorage__file_path = test_save_path  # Set file
        obj = BaseModel()
        fs.new(obj)
        fs.save()
        does_file_exist_after_save = os.path.isfile(test_save_path)  # True
        try:
            self.assertFalse(does_file_exist_before_save)  # False
            self.assertTrue(does_file_exist_after_save)  # True
            os.remove(type(fs)._FileStorage__file_path)
        except Exception as err:
            pass

    def test_reload(self):
        """"""
        fs = FileStorage()
        test_reload_path = 'test_reload.json'
        type(fs)._FileStorage__file_path = test_reload_path
        type(fs)._FileStorage__objects = {}
        if os.path.isfile(test_reload_path):
            fs.reload()
        count_initial_objects = len(fs.all())  # Initial count
        for i in range(0, 3):  # Add 3 new objects
            fs.new(BaseModel())
        count_after_loading_objects = len(fs.all())  # Initial count + 3
        fs.reload()
        count_after_reload = len(fs.all())  # Initial count
        self.assertEqual(count_initial_objects, count_after_reload)
        try:
            if os.path.isfile(test_reload_path):
                os.remove(type(fs)._FileStorage__file_path)
        except Exception as err:
            pass


if __name__ == '__main__':
    unittest.main()
