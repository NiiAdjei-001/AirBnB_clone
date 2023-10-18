#!/usr/bin/python3
"""user
"""
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
        super().__init__(self, *args, **kwargs)
        self.first_name = ""
        self.last_name = ""
        self.password = ""
        self.email = ""
