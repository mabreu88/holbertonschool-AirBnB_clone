#!/usr/bin/python3
"""Class BaseModel that defines all common attributes/methods."""
import uuid
from datetime import datetime


class BaseModel:
    """Class BaseModel"""

    def __init__(self):
        """Method that initializes the class."""
        self.updated_at = None
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

    def __str__(self):
        """Method that prints."""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Method that updates the public instance attribute."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Method that returns a dictionary containing keys/values."""
        Dictionary = {
            "__class__": __class__.__name__
        }
        Dictionary = self.__dict__.copy()
        return Dictionary
