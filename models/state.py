#!/usr/bin/python3
"""state
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State Class
    """
    
    name = ""

    def __init__(self, *args, **kwargs):
        """State(*args, **kwargs):

            Description:
                Initializes a class instance.

            Args:
                *args: a tuple of arguments (NOT USED)
                **kwargs: a dictionary of attribute values

            Implementation:
                obj = State() -- Creates a new instance of object
                ---
                obj = State(kwargs) -- Creates a new instance of object
                                           with attributes in kwargs dictionary
        """
        super().__init__(self, *args, **kwargs)
