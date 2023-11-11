#!/usr/bin/python3
"""
Conducting module for State module
"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Verifying the State module
    """
    def test_inheritance(self):
        """
        Verifying if State is a subclass of BaseModel
        """
        self.assertTrue(issubclass(State, BaseModel))

    def test_default_attribute(self):
        """
        Verifying default value for State instance
        """
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()

