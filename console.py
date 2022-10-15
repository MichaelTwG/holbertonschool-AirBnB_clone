#!/usr/bin/python3
""" Module console """

import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand inherits from cmd.Cmd """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """in quit - exit of the console"""
        return True

    def do_EOF(self, line):
        """Handle the EOF character"""
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER. """
        pass

    def do_create(self, line):
        """
            Creates an instance of the clase
            Ex: create BaseModel
        """

        if line == "" or line is None:
            print("** class name missing **")

        else:
            className = line.split()

            if className[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                new_instance = storage.classes()[className[0]]
                new_instance.save()
                print(new_instance.id)

    def do_show(self, line):
        """
            Print the string representation of an instance bassed of the id
            ex: show BaseModel 1234-1234-1234
        """
        args = line.split()
        instance_key = f"{args[0]}.{args[1]}"
        object_dict = storage.all()

        print(object_dict[instance_key])

    def do_destroy(self, line):
        """
            Delete an instance based on the class name and id.
            ex: destroy BaseModel 1234-1234-1234
        """
        if line == "" or line is None:
            print("** class name missing **")

        words = line.split(' ')

        if words[0] not in storage.classes():
            print("** class doesn't exist **")

        elif len(words) < 2:
            print("** instance id missing **")

        else:
            key = "{}.{}".format(words[1], words[2])

            if key not in storage.all().keys():
                print("** no instance found **")

            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """
            Print all of the instances of a calass
            retrived for parametter
            ex: all BaseModel
        """
        args = line.split()
        object_dict = storage.all()
        object_list = []

        if len(args) == 1:
            for key, instance in object_dict.items():

                class_of_instance = key.split(".")

                if class_of_instance[0] == args[0]:

                    object_list.append(str(instance))
            print(object_list)

    def do_update(self, line):
        """
            Update the atributes of an instance
            bassed in the arguments passed in line

            ex: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()

        if len(args) < 1:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            attribute = args[2]
            atrib_val = args[3]
            object_dict = storage.all()
            instance_key = f"{args[0]}.{args[1]}"

            object_dict[instance_key].__dict__[attribute] = atrib_val
            storage.save()
        
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
