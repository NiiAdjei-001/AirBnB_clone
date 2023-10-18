#!/usr/bin/python3
"""Base Model Module
"""
from datetime import datetime
import uuid
from models import storage
from models.base_model import BaseModel

class User(BaseModel):
    """User Class
    """

    def __init__(self, *args, **kwargs):
        """User(*args, **kwargs):

            Description:
                Initializes a class instance.

            Args:
                *args: a tuple of arguments (NOT USED)
                **kwargs: a dictionary of attribute values

            Implementation:
                obj = User() -- Creates a new instance of object
                ---
                obj = User(kwargs) -- Creates a new instance of object
                                           with attributes in kwargs dictionary
        """
        self.first_name = ""
        self.last_name = ""
        self.password = ""
        self.email = ""
        BaseModel.__init__(self, *args, **kwargs)
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
        """
