#!/usr/bin/python3
"""amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class
    """

    name = None

    def __init__(self, *args, **kwargs):
        """Amenity(*args, **kwargs):

            Description:
                Initializes a class instance.

            Args:
                *args: a tuple of arguments (NOT USED)
                **kwargs: a dictionary of attribute values

            Implementation:
                obj = Amenity() -- Creates a new instance of object
                ---
                obj = Amenity(kwargs) -- Creates a new instance of object
                                           with attributes in kwargs dictionary
        """
        super().__init__(self, *args, **kwargs)
