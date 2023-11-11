#!/usr/bin/python3
"""
Conducting tests for the Place module
"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Conducting tests for the Place module
    """
    def test_inheritance(self):
        """
        Verifying if Place is a subclass of BaseModel through testing
        """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_default_attributes(self):
        """
        Verifying the default values of the Place class.
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0)
        self.assertEqual(place.longitude, 0)
        self.assertEqual(place.amenity_ids, 0)


if __name__ == '__main__':
    unittest.main()

