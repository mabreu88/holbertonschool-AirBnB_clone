#!/usr/bin/python3
"""Review Class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Method that initializes the class."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
