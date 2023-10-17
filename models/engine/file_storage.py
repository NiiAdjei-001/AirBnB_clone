#!/usr/bin/python3
"""file_storage module
"""
import json
import os.path
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
        self.all()[key] = serialize_obj(obj)

    def save(self):
        """save():

            Description:
                Saves the content of __object dictionary into json file
        """
        with open(type(self).__file_path, 'w') as json_file:
            json.dump(type(self).__objects, json_file)

    def reload(self):
        """reload():

            Description:
                Repopulates __objects dictionary from json file
        """
        self.all().clear()
        if os.path.isfile(type(self).__file_path):
            with open(type(self).__file_path, 'r') as json_file:
                type(self).__objects = json.load(json_file)


def serialize_obj(obj):
    """serialize_obj(obj: Object):

        Description:
            Serialize Object into JSON format

        Args:
            obj: a class instance

        Return:
            Json format of object
    """
    obj_dic = obj.__dict__
    convert_datetime_to_iso(obj_dic)
    obj_dic['__class__'] = obj.__class__.__name__
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


def deserialize_obj(json_obj):
    """deserialize_obj(json_obj: dict)

        Description:
            Deserialize json object into object form

        Args:
            obj: a class instance
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
