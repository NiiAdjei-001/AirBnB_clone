#!/usr/bin/python3
import unittest
import uuid
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """Test Review Class
    """
    def test_place_id(self):
        """"""
        review = Review()
        _id = str(uuid.uuid4())
        type(review).place_id = _id
        self.assertEqual(type(review).place_id, _id)
        self.assertIs(type(type(review).place_id), str)

    def test_user_id(self):
        """"""
        review = Review()
        _id = str(uuid.uuid4())
        type(review).user_id = _id
        self.assertEqual(type(review).user_id, _id)
        self.assertIs(type(type(review).user_id), str)

    def test_text(self):
        """"""
        review = Review()
        type(review).text = 'Good. 5 star'
        self.assertEqual(type(review).text, 'Good. 5 star')
        self.assertIs(type(type(review).text), str)


if __name__ == '__main__':
    unittest.main()
