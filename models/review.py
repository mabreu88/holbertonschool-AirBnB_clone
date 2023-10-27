#!/usr/bin/python3
"""Review Class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel class."""

    self.place_id = ""
    self.user_id = ""
    self.text = ""
