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
        city.state_id = _id
        self.assertEqual(city.state_id, _id)
        self.assertIs(type(city.state_id), str)

    def test_name(self):
        """"""
        city = City()
        city.name = 'Dallas'
        self.assertEqual(city.name, 'Dallas')
        self.assertIs(type(city.name), str)


if __name__ == '__main__':
    unittest.main()
