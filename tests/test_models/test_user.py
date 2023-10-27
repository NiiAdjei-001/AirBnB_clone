#!/usr/bin/python3
import unittest
import sys
from models.user import User


class TestUserClass(unittest.TestCase):
    """Test User Class
    """
    def test_first_name(self):
        """"""
        user = User()
        type(user).first_name = 'John'
        self.assertEqual(type(user).first_name, 'John')
        self.assertIs(type(type(user).first_name), str)

    def test_last_name(self):
        """"""
        user = User()
        type(user).last_name = 'Doe'
        self.assertEqual(type(user).last_name, 'Doe')
        self.assertIs(type(type(user).last_name), str)

    def test_email(self):
        """"""
        user = User()
        type(user).email = 'John@Doe.com'
        self.assertEqual(type(user).email, 'John@Doe.com')
        self.assertIs(type(type(user).email), str)

    def test_password(self):
        """"""
        user = User()
        type(user).password = 'root'
        self.assertEqual(type(user).password, 'root')
        self.assertIs(type(type(user).password), str)


if __name__ == '__main__':
    unittest.main()
