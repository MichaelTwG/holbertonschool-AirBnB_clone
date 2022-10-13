#!/usr/bin/python3
""" Module for the entry point of the command interpreter."""


import cmd
from models.base_modeL import BaseModel
from models import storage
import re
import json

class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter. """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handles End Of File character.
        """

        print()
        return True

    def do_quit(self, line):
        """Exits the program.
        """

        return True

    def emptyline(self):
        """Doesn't do anything on ENTER. """
        pass

    def do_create(self, line):
        """Creates an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)
