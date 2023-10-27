#!/usr/bin/python3
"""Class BaseModel that defines all common attributes/methods."""
import uuid
import models
from datetime import datetime


class BaseModel:
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        """ re-create an instance """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Method that prints."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Method that updates the public instance attribute."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Method that returns a dictionary containing keys/values """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
