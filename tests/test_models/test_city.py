#!/usr/bin/python3
"""
This module performs testing for the City module
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Conducting tests on the City class
    """
    def test_inheritance(self):
        """
        Verifying if City is a subclass of BaseModel through testing
        """
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """
        Evaluating values of the City() instance through testing
        """
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_attribute_types(self):
        """
        Conducting tests for the instance type
        """
        city = City()
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.state_id, str)

    def test_str_representation(self):
        """
        Evaluating the __str__ representation of a City() class instance through testing
        """
        city = City()
        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected_str)


if __name__ == '__main__':
    unittest.main()
