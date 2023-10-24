#!/usr/bin/python3
"""State Class."""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Method that initializes the class."""
        super().__init__(*args, **kwargs)
        self.name = ""
