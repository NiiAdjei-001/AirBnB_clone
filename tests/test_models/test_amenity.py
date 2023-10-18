#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """Test Amenity Class
    """
    def test_name(self):
        """"""
        amenity = Amenity()
        amenity.name = 'Spa'
        self.assertEqual(amenity.name, 'Spa')
        self.assertIs(type(amenity.name), str)


if __name__ == '__main__':
    unittest.main()
