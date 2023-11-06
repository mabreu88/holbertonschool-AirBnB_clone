#!/usr/bin/python3
"""Test the amenity Method."""
import unittest
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """Class that tests the Amenity class"""

    def name_test(self):
        """Method that test the name."""

        test = Amenity()
        self.assertEqual(test.name, '')
