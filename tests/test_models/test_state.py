#!/usr/bin/python3
import unittest
from models.state import State


class TestStateClass(unittest.TestCase):
    """Test State Class
    """
    def test_State(self):
        """"""
        state = State()
        type(state).name = None
        state.name = 'John'
        self.assertIsNone(type(state).name)
        self.assertIsNot(state.name, type(state).name)
    
    def test_name(self):
        """"""
        state = State()
        type(state).name = None
        state.name = 'John'
        self.assertIsNone(type(state).name)
        self.assertIsNot(state.name, type(state).name)

    def test_state(self):
        """"""
        state = State()
        type(state).name = None
        state.name = 'John'
        self.assertIsNone(type(state).name)
        self.assertIsNot(state.name, type(state).name)


if __name__ == '__main__':
    unittest.main()
