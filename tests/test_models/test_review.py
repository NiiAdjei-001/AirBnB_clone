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
        review.place_id = _id
        self.assertEqual(review.place_id, _id)
        self.assertIs(type(review.place_id), str)

    def test_user_id(self):
        """"""
        review = Review()
        _id = str(uuid.uuid4())
        review.user_id = _id
        self.assertEqual(review.user_id, _id)
        self.assertIs(type(review.user_id), str)

    def test_text(self):
        """"""
        review = Review()
        review.text = 'Good. 5 star'
        self.assertEqual(review.text, 'Good. 5 star')
        self.assertIs(type(review.text), str)


if __name__ == '__main__':
    unittest.main()
