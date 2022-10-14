#!/usr/bin/python3
""" Module for the entry point of the command interpreter."""


import cmd
from models.base_model import BaseModel
from models import storage
import re
import json

class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter. """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handles End Of File character."""

        print()
        return True

    def do_quit(self, line):
        """Exits the program."""

        return True

    def emptyline(self):
        """Doesn't do anything on ENTER. """
        pass

    def do_create(self, line):
        """Creates an instance."""
        if line == "" or line is None:
            print("** class name missing **")

        className = line.split(" ")
        if className[1] not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes(className[1])
            b.save()
            print(b.id)

    def do_destroy(self, line):
        """ delete an instance based on the class name and id. """
        if line == "" or line is None:
             print("** class name missing **")
        else:
            words = line.split(' ')
            if words[1] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 3:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[1], words[2])
                if key not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()
