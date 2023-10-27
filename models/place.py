#!/usr/bin/python3
"""place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place Class
    """

    city_id = None
    user_id = None
    name = None
    description = None
    number_rooms = None
    number_bathrooms = None
    max_guest = None
    price_by_night = None
    latitude = None
    longitude = None
    amenity_ids = None

    def __init__(self, *args, **kwargs):
        """Place(*args, **kwargs):

            Description:
                Initializes a class instance.

            Args:
                *args: a tuple of arguments (NOT USED)
                **kwargs: a dictionary of attribute values

            Implementation:
                obj = Place() -- Creates a new instance of object
                ---
                obj = Place(kwargs) -- Creates a new instance of object
                                           with attributes in kwargs dictionary
        """
        super().__init__(self, *args, **kwargs)
