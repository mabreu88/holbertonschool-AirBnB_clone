#!/usr/bin/python3
"""Test the state Method."""
import unittest
from models.state import State


class Test_state(unittest.TestCase):
    """Class that tests the state class"""

    def name_test(self):
        """Method that test the name."""

        test = State()
        self.assertEqual(test.name, '')
