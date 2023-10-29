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
        self.assertNotEqual(first_updated, my_object.updated_at)

    def another_save_test(self):
        """Method that test the save Method."""
        save_test = BaseModel()
        self.assertIsInstance(save_test, BaseModel)


    def to_dict_test(self):
        """Method that test the to_dicte Method."""
        dict_method = BaseModel()
        keys = ['id', 'created_at', 'updated_at', '__class__']
        dict_result = dict_method.to_dict()
        for key in keys:
            self.assertIn(key, dict_result)

    def self_id_test(self):
        """Method that test the id attribute to be string."""
        attribute_id = BaseModel()
        self.assertIsInstance((attribute_id.id), str)

    def created_at_test(self):
        """Method that test the created_at attribute."""
        attribute_created_at = BaseModel()
        self.assertIsInstance(attribute_created_at, BaseModel)

    def str_test(self):
        """Method that test the str method."""
        str_method = BaseModel()
        my_dict = str_method.__dict__
        string1 = "[BaseModel] ({}) {}".format(str_method.id, my_dict)
        string2 = str(str_method)
        self.assertEqual(string1, string2)

if __name__ == '__main__':
    unittest.main()
