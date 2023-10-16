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
        """Create a new instance of a class.
            Arg:
                arg: a string of parameters

            Return:
                return object's id

            Implementation:
                $ create <class name>
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
        """Displays an instance of a class
            Arg:
                arg: a string of parameters

            Implementation:
                $ show <class name> <object id>
        """
        argv = parse(arg)
        if len(argv) == 0:
            print("** class name missing **")
            return
        if len(argv) >= 1:
            if (argv[0] == "BaseModel"):
                if (len(argv) > 1):
                    print(BaseModel.storage)
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
