#!/usr/bin/python3
""" Class FileStorage. """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ Class that serializes instances to a JSON file and deserializes. """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Method all that returns the dictionary. """
        return FileStorage.__objects

    def new(self, obj):
        """ Method new that sets in the dictionary the key.id. """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """ Method save that serializes the directory to the json file. """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f, indent=4)

    def reload(self):
        """ Method reload that deserializes the json file. """
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review
        }
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for x in objdict.values():
                    clas_name = x["__class__"]
                    del x["__class__"]
                    self.new(classes[clas_name](**x))
        except FileNotFoundError:
            return
