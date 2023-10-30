#!/usr/bin/python3
"""Test the user Method."""
import unittest
from models.user import User


class Test_user(unittest.TestCase):
    """Class that tests the user class"""

    def name_test(self):
        """Method that test the name."""

        test = User()
        self.assertEqual(test.name, '')

    def email_test(self):
        """Method that checks the email."""

        test = User()
        self.assertEqual(test.email, '')

    def password_test(self):
        """Method that checks the password."""

        test = User()
        self.assertEqual(test.password, '')

    def first_name_test(self):
        """Method that checks the first name."""

        test = User()
        self.assertEqual(test.first_name, '')

    def last_name_test(self):
        """Method that checks the last_name."""

        test = User()
        self.assertEqual(test.last_name, '')
