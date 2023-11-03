#!/usr/bin/python3
import unittest
import sys

class TestConsoleClass(unittest.TestCase):
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd("help show")
    """Test Console Class
    """
    def test_quit(self):
        """Test quit function
        """
        pass

