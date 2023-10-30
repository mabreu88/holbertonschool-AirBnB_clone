#!/usr/bin/python3
"""Test the Review Method."""
import unittest
from models.review import Review


class Test_Review(unittest.TestCase):
    """Class that tests the Review class"""

    def name_test(self):
        """Method that test the name."""

        test = Review()
        self.assertEqual(test.name, '')
