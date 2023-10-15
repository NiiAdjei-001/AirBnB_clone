#!/usr/bin/python3
"""File storage module
"""
import json
import os.path


class FileStorage:
    """File Storage Class
    """

    def __init__(self, filepath='file.json', obj={}):
        """
        """
        self.__file_path = filepath
        self.__objects = obj

    def all(self):
        """Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """Sets a new object 'obj' into the __objects dictionary
        """
        key = "{}.{}".format(obj['__class__'], obj['id'])
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects list to the JSON file(path:__file_path)
        """
        with open(self.__file_path, 'w') as json_file:
            json.dump(self.__objects, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as json_file:
                self.__objects = json.load(json_file)
