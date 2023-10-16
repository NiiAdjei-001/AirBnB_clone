#!/usr/bin/python3
import unittest
import sys
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Base Model Test Class
    """
    def test__str__(self):
        """Test __str__() method to ensure it generates the desired pattern
            of [<object class>] (<object id>) <object attributes>
        """
        obj = BaseModel()
        class_name = obj.__class__.__name__
        self_id = obj.id
        self_attr = obj.__dict__
        string_format = "[{}] ({}) {}".format(class_name, self_id, self_attr)
        self.assertEqual(obj.__str__(), string_format)

    def test_id_instantiation(self):
        """Test obj.id is not None, ""
        """
        obj = BaseModel()
        val = [None, ""]
        self.assertNotIn(obj, val)
 
    def test_id_type(self):
        """Test obj.id is of type str
        """
        obj = BaseModel()
        self.assertIs(type(obj.id), str)

    def test_save(self):
        """
        """
        pass

    def test_to_dict(self):
        """
        """


if __name__ == '__main__':
    unittest.main()
