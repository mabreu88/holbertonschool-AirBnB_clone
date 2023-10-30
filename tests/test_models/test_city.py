#!/usr/bin/python3
"""Test the city Method."""
import unittest
from models.city import City


class Test_City(unittest.TestCase):
    """Class that tests the City class"""

    def name_test(self):
        """Method that test the name."""

        test = City()
        self.assertEqual(test.name, '')
