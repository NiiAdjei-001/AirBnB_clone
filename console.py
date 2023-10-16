#!/usr/bin/python3
"""AirBnB Console Module
"""
import sys
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class: Command line shell interpreter interface for
        testing.
    """
    intro = ''
    prompt = '(hbnb)'

    def emptyline(self):
        """On empty line, do nothing"""
        pass

    def do_create(self, arg):
        """Create an object based of a class name and id.
            Arg:
                arg: <class name>

            Return:
                return object id

            Implementation:
                $ create <class name>
                $ create User
        """
        argv = parse(arg)
        if len(argv) == 0:
            print("** class name missing **")
            return
        if len(argv) == 1:
            if (argv[0] == "BaseModel"):
                obj = BaseModel()
                print(obj.id)
                obj.save()
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Displays an instance based of a class name and id
            Arg:
                arg: <class name> <object id>

            Implementation:
                $ show <class name> <object id>
                $ show User fe15e5e2d6e2d6e2de6d6ed
        """
        argv = parse(arg)
        if len(argv) == 0:
            print("** class name missing **")
            return
        if len(argv) >= 1:
            if (argv[0] == "BaseModel"):
                if (len(argv) > 1):
                    key = "{}.{}".format(argv[0], argv[1])
                    if (key in storage.all()):
                        print("console Checker:", storage.all()[key])
                        obj = BaseModel(storage.all()[key])
                        print(obj.__str__())
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on a class name and id
            Arg:
                arg: <class name> <object id>

            Implementation:
                $ destroy <class name> <object id>
                $ destroy User fe15e5e2d6e2d6e2de6d6ed
        """
        argv = parse(arg)
        if len(argv) == 0:
            print("** class name missing **")
            return
        if (argv[0] == "BaseModel"):
            if (len(argv) > 1):
                key = "{}.{}".format(argv[0], argv[1])
                if (key in storage.all()):
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_EOF(self, line):
        """Exit on 'end of line' from console"""
        return True

    def do_quit(self, line):
        """Exit from console"""
        return True


def parse(arg):
    """Converts a series of strings to an argument tuple"""
    return tuple(arg.split())


if __name__ == '__main__':
    print(dir(storage))
    HBNBCommand().cmdloop()
