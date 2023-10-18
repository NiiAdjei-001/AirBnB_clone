#!/usr/bin/python3
"""city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City Class
    """

    def __init__(self, *args, **kwargs):
        """City(*args, **kwargs):

            Description:
                Initializes a class instance.

            Args:
                *args: a tuple of arguments (NOT USED)
                **kwargs: a dictionary of attribute values

            Implementation:
                obj = City() -- Creates a new instance of object
                ---
                obj = City(kwargs) -- Creates a new instance of object
                                           with attributes in kwargs dictionary
        """
        super().__init__(self, *args, **kwargs)
        self.state_id = ""
        self.name = ""
