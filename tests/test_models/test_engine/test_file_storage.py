#!/usr/bin/python3
"""Test to test the file storage method."""
import unittest
import os
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class Test_file_storage(unittest.TestCase):
    """Class that test the file storage."""

    def file_test(self):
        """Method that checks the file."""

        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def doc_test(self):
        """Test that checks the documentation."""

        self.assertTrue(len(FileStorage.__doc__) > 0)

    def all_test(self):
        """Test the all method."""

        test = FileStorage()
        self.assertEqual(type(test.all()), dict)

    def new_test(self):
        """Test the new method."""

        test = FileStorage()
        test.all().clear()
        test_base_model = BaseModel()
        test.new(test_base_model)
        self.assertNotEqual(len(test.all()), 0)

    def save_test(self):
        """Test the save method."""

        test = FileStorage()
        test.all().clear()
        test_base_model = BaseModel()
        test.new(test_base_model)
        self.assertNotEqual(len(test.all()), 0)

    def reload_test(self):
        """Test the reload method."""

        test = FileStorage()
        test.all().clear()
        test.reload()
        self.assertNotEqual(len(test.all()), 0)

if __name__ == '__main__':
    unittest.main()
