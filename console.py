#!/usr/bin/python3
"""Airnbnb project console."""
import cmd
import re
import json

from shlex import split
from models.engine.file_storage import FileStorage
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
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def emptyline(self):
        """Method that creates an emppty line."""
        pass

    def do_create(self, arg):
        """Method that creates a new instance of BaseModel."""
        if not arg:
            print("** class name missing **")
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            for key, val in self.__classes.items():
                if key == arg:
                    instance = self.__classes[key](val)
                    FileStorage.save(instance)
            print(f"{instance.id}")

    def do_show(self, arg):
        """Method that prints the string representation of an instance."""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in self.__classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                all_objects = storage.all()
                if key in all_objects:
                    print(all_objects[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Method that deletes instances based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in self.__classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                all_objects = storage.all()
                if key in all_objects:
                    del all_objects[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Method that prints all string representation of all instances"""
        if not arg:
            all_objets = storage.all()
            for key, obj in all_objets.items():
                print(obj)
        else:
            args = arg.split()
            if args[0] not in self.__classes:
                print("** class doesn't exist **")
            else:
                all_objects = storage.all()
                for obj_key, obj in all_objects.items():
                    if obj_key.split('.')[0] == args[0]:
                        print(obj)

    def do_update(self, arg):
        """Method that updates an instance."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objects = storage.all()
            if key not in all_objects:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attribute_name = args[2]
                attribute_value = args[3]
                instance = all_objects.get[key]
            if hasattr(instance, attribute_name):
                attr_type = type(getattr(instance, attribute_name))
                try:
                    casted_value = attr_type(attribute_value)
                    setattr(instance, attribute_name, casted_value)
                    instance.save()
                except (ValueError, TypeError):
                    print("** invalid value **")
            else:
                print("** attribute name doesn't exist **")

    def do_quit(self, arg):
        """Method that quits the program."""
        return True

    def do_EOF(self, arg):
        """Method for the end of file."""
        return True

    def help_quit(self):
        """Method that manages the help for the commands.s"""
        print("Quit command to exit the program.")

    def help_create(self):
        """Method that manages the help commando for the create method."""
        print("Create command to create a new insance.")

    def help_show(self):
        """Method that manages the help command for the show method."""
        print("Show command prints on screen infromation about instances.")

    def help_destroy(self):
        """Method that manages the help command for the destroy method."""
        print("Destroy command deletes instances.")

    def help_all(self):
        """Method that manages the help command for the all method."""
        print("All command displays all of the instances.")

    def help_EOF(self):
        """Method that manages the help command for the EOF method."""
        print("EOF command exits the program.")

    def help_update(self):
        """ Method that manages the help command for the update method. """
        print("The Update command updates the class information.")


if __name__ == '__main__':

    HBNBCommand().cmdloop()
