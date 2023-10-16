#!/usr/bin/python3
"""Base Model Module
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """Base Model Class
    """

    def __init__(self, *args, **kwargs):
        """BaseModel(): Method used to initialize BaseModel object.

            Args:
                *args: a tuple of arguments (NOT USED)
                **kwargs: a dictionary of attribute values

            Implementation:
                obj = BaseModel() -- Creates a new instance of object
                ---
                obj = BaseModel(kwargs) -- Creates a new instance of object
                                           with attributes in kwargs dictionary
        """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            for key, val in kwargs.items():
                if key == '__class__':
                    pass
                elif key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(val))
                else:
                    setattr(self, key, val)

    def __str__(self):
        """__str__(): Method used to get a string representation of
                        an instance of class BaseModel
            Returns:
                format => "[<object class>] (<object id>) <object attributes>"
        """
        class_name = self.__class__.__name__
        self_id = self.id
        self_attributes = self.__dict__
        return "[{}] ({}) {}".format(class_name, self_id, self_attributes)

    def save(self):
        """save(): Method used to save changes of BaseModel instance.
                    Changes are saved into the json file directly

            Implementation:
                obj = BaseModel()
                obj.name = "Quirgmire"
                obj.save()
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """to_dict(): Method used to convert BaseModel object into a dictionary
                        object
        """
        obj = {**(self.__dict__)}
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = obj['created_at'].isoformat()
        obj['updated_at'] = obj['updated_at'].isoformat()
        return obj
