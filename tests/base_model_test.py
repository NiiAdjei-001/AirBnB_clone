#!/usr/bin/python3
import unittest
import sys
sys.path.append('..')
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    def setUp(self):
        print("\nRunning setUp method...")
        self.model1 = BaseModel()
        self.model2 = BaseModel()
    
    def test_basemodel_instantiation(self):
        print("Running Test case")
        self.assertIsNot(self.model1, self.model2)

    def tearDown(self):
        print("Running tearDown method...")

if __name__ == '__main__':
    unittest.main()
