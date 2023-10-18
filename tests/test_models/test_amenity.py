#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """Test Amenity Class
    """
    def test_name(self):
        """"""
        amenity = Amenity()
        type(amenity).name = 'Spa'
        self.assertEqual(type(amenity).name, 'Spa')
        self.assertIs(type(type(amenity).name), str)


if __name__ == '__main__':
    unittest.main()
