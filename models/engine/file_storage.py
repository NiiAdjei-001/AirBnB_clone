#!/usr/bin/python3
"""file_storage module
"""
import sys
import os
import json
from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review
from datetime import datetime


class FileStorage:
    """FileStorage Class
    """
    __file_path = "file.json"  # file path for json file which will store data
    __objects = {}  # dictionary variable to store the content of stored data

    def __init__(self):
        """
        """
        pass

    def all(self):
        """all():

            Description:
                Returns the __object dictionary

            Return: __objects
        """
        return type(self).__objects

    def new(self, obj):
        """new(obj: Object):

            Description:
                Adds a new serialized object into __objects dictionary

            Args:
                obj: An object instance
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.all()[key] = obj.to_dict()

    def save(self):
        """save():

            Description:
                Saves the content of __object dictionary into json file
        """
        json_obj = {}
        for key, obj_dic in self.all().items():
            json_obj[key] = serialize(obj_dic)
        with open(type(self).__file_path, 'w') as json_file:
            json.dump(json_obj, json_file)

    def reload(self):
        """reload():

            Description:
                Repopulates __objects dictionary from json file
        """
        self.all().clear()
        if os.path.isfile(type(self).__file_path):
            with open(type(self).__file_path, 'r') as json_file:
                for key, val in json.load(json_file).items():
                    self.all()[key] = deserialize(val)


def serialize(obj_dic):
    """serialize(obj: Object):

        Description:
            Serialize Object into JSON format

        Args:
            obj_dic: an object dict

        Return:
            Json format of object
    """
    convert_datetime_to_iso(obj_dic)
    return obj_dic


def convert_datetime_to_iso(obj_dic, list_attributes=None):
    """convert_datetime_to_iso(obj_dic: dict, list_attributes: list):

        Description:
            Converts all datetime datatypes in an object dictionary to
            isoformat

        Args:
            obj_dic: object dictionary
            list_attributes: list of attributes to convert to isoformat
    """
    if (list_attributes is None):
        """Iterate through all attributes and convert"""
        for key, val in obj_dic.items():
            if type(val) is datetime:
                obj_dic[key] = val.isoformat()
    else:
        """convert only specified fields"""
        for attr in list_attributes:
            if (attr in obj_dic.keys()):
                val = obj_dic[attr]
                if type(val) is datetime:
                    obj_dic[attr] = val.isoformat()


def deserialize(json_obj):
    """deserialize(json_obj: dict)

        Description:
            Deserialize json obj

        Args:
            json_str: a string in json format

        Return:

    """
    convert_iso_to_datetime(json_obj)
    return json_obj


def convert_iso_to_datetime(json_obj, list_attribute=None):
    """convert_iso_to_datetime(obj_dic, list_attributes):

        Description:
            Converts all iso date fields into datetime data type

        Args:
            json_obj: json object
            list_attributes: List of attributes to convert to datetime format
    """
    for key, val in json_obj.items():
        """Convert datetime data attributes from iso format"""
        try:
            json_obj[key] = (datetime.fromisoformat(val))
        except ValueError:
            pass
        except TypeError:
            pass


def print_pretty(json_str):
    print(json.dumps(json_str, indent=4))
