#!/usr/bin/python3
"""Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Method that initializes the class."""
        super().__init__(*args, **kwargs)
        self.name = ""
