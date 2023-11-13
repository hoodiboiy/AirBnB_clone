#!/usr/bin/python3
"""
Performing tests on the Amenity module
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Conducting tests on the Amenity class module
    """
    def test_inheritance(self):
        """
        Verifying if Amenity is a subclass of the BaseModel class through testing
        """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_default_attribute(self):
        """
        Evaluating the value of the Amenity instance through testing
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
