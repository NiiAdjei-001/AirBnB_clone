#!/usr/bin/python3
import unittest
import uuid
from models.city import City


class TestCityClass(unittest.TestCase):
    """Test City Class
    """
    def test_state_id(self):
        """"""
        city = City()
        _id = str(uuid.uuid4())
        type(city).state_id = _id
        self.assertEqual(type(city).state_id, _id)
        self.assertIs(type(type(city).state_id), str)

    def test_name(self):
        """"""
        city = City()
        type(city).name = 'Dallas'
        self.assertEqual(type(city).name, 'Dallas')
        self.assertIs(type(type(city).name), str)


if __name__ == '__main__':
    unittest.main()
