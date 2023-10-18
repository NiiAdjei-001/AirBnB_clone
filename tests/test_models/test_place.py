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
        place.city_id = _id
        self.assertEqual(place.city_id, _id)
        self.assertIs(type(place.city_id), str)

    def test_user_id(self):
        """"""
        place = Place()
        _id = str(uuid.uuid4())
        place.user_id = _id
        self.assertEqual(place.user_id, _id)
        self.assertIs(type(place.user_id), str)

    def test_name(self):
        """"""
        place = Place()
        place.name = 'Crib'
        self.assertEqual(place.name, 'Crib')
        self.assertIs(type(place.name), str)

    def test_description(self):
        """"""
        place = Place()
        place.description = 'luxurious'
        self.assertEqual(place.description, 'luxurious')
        self.assertIs(type(place.description), str)

    def test_number_rooms(self):
        """"""
        place = Place()
        place.number_rooms = 5
        self.assertEqual(place.number_rooms, 5)
        self.assertIs(type(place.number_rooms), int)

    def test_number_bathrooms(self):
        """"""
        place = Place()
        place.number_bathrooms = 5
        self.assertEqual(place.number_bathrooms, 5)
        self.assertIs(type(place.number_bathrooms), int)

    def test_max_guest(self):
        """"""
        place = Place()
        place.max_guest = 5
        self.assertEqual(place.max_guest, 5)
        self.assertIs(type(place.max_guest), int)

    def test_price_by_night(self):
        """"""
        place = Place()
        place.price_by_night = 500
        self.assertEqual(place.price_by_night, 500)
        self.assertIs(type(place.price_by_night), int)

    def test_latitude(self):
        """"""
        place = Place()
        place.latitude = 102.202
        self.assertAlmostEqual(place.latitude, 102.202)
        self.assertIs(type(place.latitude), float)

    def test_latitude(self):
        """"""
        place = Place()
        place.longitude = 102.202
        self.assertAlmostEqual(place.longitude, 102.202)
        self.assertIs(type(place.longitude), float)

    def test_amenity_ids(self):
        """"""
        place = Place()
        place.amenity_ids = [str(uuid.uuid4()), str(uuid.uuid4())]
        # print(place.amenity_ids)
        self.assertIs(type(place.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
