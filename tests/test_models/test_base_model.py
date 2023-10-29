#!/usr/bin/python3
"""BaseModel test."""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class Test_base_model(unittest.TestCase):
    """Class that test the BaseModel class."""

    def save_test(self):
        """Method that test the save Method."""
        my_object = BaseModel()
        first_updated = my_object.updated_at
        my_object.save()
        second_updated = my_object.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def to_dict_test(self):
        """Method that test the to_dicte Method."""
        dict_method = BaseModel()
        dict_result = dict_method.to_dict()
        self.assertIsInstance(dict_result, dict)

    def self_id_test(self):
        """Method that test the id attribute."""
        attribute_id = BaseModel()
        self.assertEqual(type(attribute_id.id), str)

    def created_at_test(self):
        """Method that test the created_at attribute."""
        attribute_created_at = BaseModel()
        self.assertIsInstance(attribute_created_at, BaseModel)

    def str_test(self):
        """Method that test the str method."""
        str_method = BaseModel()
        self.assertEqual(type(str_method.__str__), str)

if __name__ == '__main__':
    unittest.main()
