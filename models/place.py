#!/usr/bin/python3
"""place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place Class
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude =0.0
    amenity_ids = []
    
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
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude =0.0
        self.amenity_ids = []
