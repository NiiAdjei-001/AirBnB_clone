#!/usr/bin/python3
"""user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class
    """
    first_name = None
    last_name = None
    password = None
    email = None

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
        super().__init__(self, *args, **kwargs)
