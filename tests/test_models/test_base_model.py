#!/usr/bin/python3
import unittest
import sys
from models.base_model import BaseModel
from datetime import datetime


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
        self.assertIs(type(string_format), str)

    def test_id_instantiation(self):
        """Test obj.id is not None, ""
        """
        obj = BaseModel()
        val = [None, ""]
        self.assertNotIn(obj, val)

    def test__init__(self):
        """Test obj.id is of type str
        """
        obj = BaseModel()
        self.assertIs(type(obj.id), str)
        self.assertIs(type(obj.created_at), datetime)

    def test_save(self):
        """
        """
        obj = BaseModel()
        obj.save()
        self.assertIs(type(obj.updated_at), str)
        d_json = obj.to_dict()
        self.assertIs(type(d_json['updated_at']), str)

    def test_to_dict(self):
        """
        """
        obj = BaseModel()
        obj.updated_at = datetime.utcnow()
        dict_json = obj.to_dict()
        self.assertIs(type(dict_json), dict)
        self.assertIs(type(dict_json['id']), str)
        self.assertIs(type(dict_json['created_at']), datetime)
        self.assertIs(type(dict_json['__class__']), str)
        self.assertEqual(dict_json['__class__'], obj.__class__.__name__)


if __name__ == '__main__':
    unittest.main()
