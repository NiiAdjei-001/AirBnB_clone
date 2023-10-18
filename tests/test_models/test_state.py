#!/usr/bin/python3
import unittest
from models.state import State


class TestStateClass(unittest.TestCase):
    """Test State Class
    """
    def test_name(self):
        """"""
        state = State()
        state.name = 'Texas'
        self.assertEqual(state.name, 'Texas')
        self.assertIs(type(state.name), str)


if __name__ == '__main__':
    unittest.main()
