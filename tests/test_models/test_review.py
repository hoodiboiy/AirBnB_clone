#!/usr/bin/python3
"""
Conducting tests for the Review module
"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Conducting tests for the Review module
    """
    def test_inheritance(self):
        """
        Verifying if Review is a subclass of BaseModel through testing
        """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_default_attributes(self):
        """
        Verifying the default values of a Review instance
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()

