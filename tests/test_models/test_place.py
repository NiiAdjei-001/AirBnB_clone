#!/usr/bin/python3
import unittest
import uuid
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    """Test Place Class
    """
    def test_city_id(self):
        """"""
        place = Place()
        _id = str(uuid.uuid4())
        type(place).city_id = _id
        self.assertEqual(type(place).city_id, _id)
        self.assertIs(type(type(place).city_id), str)

    def test_user_id(self):
        """"""
        place = Place()
        _id = str(uuid.uuid4())
        type(place).user_id = _id
        self.assertEqual(type(place).user_id, _id)
        self.assertIs(type(type(place).user_id), str)

    def test_name(self):
        """"""
        place = Place()
        type(place).name = 'Crib'
        self.assertEqual(type(place).name, 'Crib')
        self.assertIs(type(type(place).name), str)

    def test_description(self):
        """"""
        place = Place()
        type(place).description = 'luxurious'
        self.assertEqual(type(place).description, 'luxurious')
        self.assertIs(type(type(place).description), str)

    def test_number_rooms(self):
        """"""
        place = Place()
        type(place).number_rooms = 5
        self.assertEqual(type(place).number_rooms, 5)
        self.assertIs(type(type(place).number_rooms), int)

    def test_number_bathrooms(self):
        """"""
        place = Place()
        type(place).number_bathrooms = 5
        self.assertEqual(type(place).number_bathrooms, 5)
        self.assertIs(type(type(place).number_bathrooms), int)

    def test_max_guest(self):
        """"""
        place = Place()
        type(place).max_guest = 5
        self.assertEqual(type(place).max_guest, 5)
        self.assertIs(type(type(place).max_guest), int)

    def test_price_by_night(self):
        """"""
        place = Place()
        type(place).price_by_night = 500
        self.assertEqual(type(place).price_by_night, 500)
        self.assertIs(type(type(place).price_by_night), int)

    def test_latitude(self):
        """"""
        place = Place()
        type(place).latitude = 102.202
        self.assertAlmostEqual(type(place).latitude, 102.202)
        self.assertIs(type(type(place).latitude), float)

    def test_latitude(self):
        """"""
        place = Place()
        type(place).longitude = 102.202
        self.assertAlmostEqual(type(place).longitude, 102.202)
        self.assertIs(type(type(place).longitude), float)

    def test_amenity_ids(self):
        """"""
        place = Place()
        type(place).amenity_ids = [str(uuid.uuid4()), str(uuid.uuid4())]
        # print(place.amenity_ids)
        self.assertIs(type(type(place).amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
