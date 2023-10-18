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
        user.first_name = 'John'
        self.assertEqual(user.first_name, 'John')
        self.assertIs(type(user.first_name), str)

    def test_last_name(self):
        """"""
        user = User()
        user.last_name = 'Doe'
        self.assertEqual(user.last_name, 'Doe')
        self.assertIs(type(user.last_name), str)

    def test_email(self):
        """"""
        user = User()
        user.email = 'John@Doe.com'
        self.assertEqual(user.email, 'John@Doe.com')
        self.assertIs(type(user.email), str)

    def test_password(self):
        """"""
        user = User()
        user.password = 'root'
        self.assertEqual(user.password, 'root')
        self.assertIs(type(user.password), str)



if __name__ == '__main__':
    unittest.main()
