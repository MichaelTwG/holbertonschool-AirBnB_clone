#!/usr/bin/python3
""" Module console """

import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand inherits from cmd.Cmd """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """in quit - exit of the console"""
        return True

    def do_EOF(self, arg):
        """Handle the EOF character"""
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER. """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
