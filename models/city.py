#!/usr/bin/python3
"""Class city."""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Method that initializes the class."""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
