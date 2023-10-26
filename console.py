#!/usr/bin/python3
"""Airnbnb project console."""
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
    """Class that manages the console."""

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

    def do_create(self, arg):
        """Method that creates a new instance of BaseModel."""
        if not arg:
            print("** class name missing **")
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            instance = BaseModel
            json.dump(instance)
            print(f"{instance.id}")

    def do_show(self, arg):
        """Method that prints the string representation of an instance."""
        _input = arg.split()
        if not _input:
            print("** class name missing **")
        elif _input[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(_input) < 2:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Method that deletes instances based on the class name and id"""
        _input = arg.split()
        if not _input:
            print("** class name missing **")
        elif _input[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(_input) < 2:
            print("** instance id missing **")

    def do_all(self):
        """Method that prints all string representation of all instances"""

    def emptyline(self):
        """Method that creates an emppty line."""
        pass

    def do_quit(self, arg):
        """Method that quits the program."""
        return True

    def do_EOF(self, arg):
        """Method for the end of file."""
        return True

    def help_quit(self):
        """Method that manages the help for the commands.s"""
        print("Prendiste fuego todo, sali cagando")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
