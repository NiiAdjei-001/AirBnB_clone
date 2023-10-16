#!/usr/bin/python3
"""File storage module
"""
import json
import os.path


class FileStorage:
    """File Storage Class
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        """
        pass

    def all(self):
        """Returns the dictionary __objects
        """
        return type(self).__objects

    def new(self, obj):
        """Sets a new object 'obj' into the __objects dictionary
            Args:
                obj: An object instance
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.all()[key] = obj

    def save(self):
        """Serializes __objects list to the JSON file(path:__file_path)
        """
        with open(type(self).__file_path, 'w') as json_file:
            json.dump(type(self).__objects, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects
        """
        if os.path.isfile(type(self).__file_path):
            with open(type(self).__file_path, 'r') as json_file:
                type(self).__objects = json.load(json_file)
