#!/usr/bin/python3
import unittest
import sys
from models.engine.file_storage import FileStorage


class TestFileStorageClass(unittest.TestCase):
    """Test FileStorage Class
    """
    def test_filepath_is_valid(self):
        """"""
        fs = FileStorage()
        self.assertEqual(fs._FileStorage__file_path, 'file.json')
        
    def test_filepath_is_invalid(self):
        """"""
        pass

    def test_filepath_is_undefined(self):
        """"""
        pass

    def test_all_function_type(self):
        """"""
        fs = FileStorage()
        objs = fs.all()
        self.assertIs(type(objs), dict)

    def test_all_function_key_value(self):
        fs = FileStorage()
        objs = fs.all()
        for key, value in objs.items():
            self.assertIs(type(key), str)
            self.assertIs(type(value), dict)
            key_format = "{}.{}".format(value['__class__'],value['id'])
            self.assertEqual(key, key_format)

    def test_new_function(self):
        pass

    def test_save_function(self):
        pass

    def test_reload_function(self):
        pass


if __name__ == '__main__':
    unittest.main()
