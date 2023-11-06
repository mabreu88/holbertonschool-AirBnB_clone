#!/usr/bin/python3
"""Test the place Method."""
import unittest
from models.place import Place


class Test_place(unittest.TestCase):
    """Class that tests the place class"""

    def name_test(self):
        """Method that test the name."""

        test = Place()
        self.assertEqual(test.name, '')
