#!/usr/bin/python3
"""base_model
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """BaseModel Class
    """

    def __init__(self, *args, **kwargs):
        """BaseModel(*args, **kwargs):

            Description:
                Initializes a class instance.

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
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(val))
                elif key == '__class__':
                    pass
                else:
                    setattr(self, key, val)

    def __str__(self):
        """__str__():

            Description:
                Returns a string representation of an object of BaseModel

            Returns:
                "[<object class>] (<object id>) <object attributes>"
        """
        class_name = self.__class__.__name__
        self_id = self.id
        self_attributes = self.__dict__
        return "[{}] ({}) {}".format(class_name, self_id, self_attributes)

    def save(self):
        """save():

            Description:
                Save current state of the object.

            Implementation:
                obj = BaseModel()
                obj.name = "Quirgmire"
                obj.save()
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """to_dict():

            Description:
                Method used to convert BaseModel object into a dictionary
                object
        """
        obj_dict = {**(self.__dict__)}
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = datetime.isoformat(self.created_at)
        obj_dict['updated_at'] = datetime.isoformat(self.updated_at)
        return obj_dict
