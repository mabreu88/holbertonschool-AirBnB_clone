#!/usr/bin/python3
import cmd
import re

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    __classes = {
        "BaseModel"
        "User"
        "State"
        "City"
        "place"
        "Amenity"
        "Review"
    }

    def emptyline(self):
        pass

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def help_quit(self):
        print("Prendiste fuego todo, sali cagando")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
