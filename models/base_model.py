#!/usr/bin/python3
"""Base Model Module
"""
import datetime
import uuid
from models import storage


class BaseModel:
    """Base Model Class
    """

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel Object
        """
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == '__class__':
                    pass
                elif k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self.to_dict())

    def __str__(self):
        """Returns a string representation of the BaseModel object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Saves changes to BaseModel Object
        """
        self.updated_at = datetime.datetime.now()
        storage.new(self.to_dict())
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel object
        """
        element = {**(self.__dict__)}
        element['__class__'] = self.__class__.__name__
        element['created_at'] = element['created_at'].isoformat()
        element['updated_at'] = element['updated_at'].isoformat()
        return element
