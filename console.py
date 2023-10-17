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
        """emptyline()

            Description:
                On empty line, do nothing
        """
        pass

    def do_create(self, arg):
        """create(arg):

            Description:
                Create an object of a given class
            Arg:
                arg: <class name>

            Return:
                Return object id

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
        """show(arg):

            Description:
                Displays an object referenced by a given id
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
                        obj = BaseModel(**(storage.all()[key]))
                        print(str(obj))
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """destroy(arg):

            Description:
                Deletes an instance based on a class name and id

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

    def do_all(self, arg):
        """all(arg):

            Description:
                Prints all objects. Can be filtered according to class.

            Arg:
                arg: <class name>

            Implementation:
                $ all                  # Prints all objects
                ---
                $ all <class name>     # Prints objects of given class
                $ all User
        """
        def get_str(obj):
            """"""
            return str(parse_json_to_class_object(obj))

        argv = parse(arg)
        if len(argv) == 0:
            print(list(map(get_str, storage.all().values())))
        else:
            if argv[0] in _built_in_classes:
                objs = storage.all().values()
                objs = list(filter(lambda o: o['__class__'] == argv[0], objs))
                objs = list(map(get_str, objs))
                print(objs)
            else:
                print("** class doesn't exist **")

    def do_EOF(self, line):
        """Exit on 'end of line' from console"""
        return True

    def do_quit(self, line):
        """Exit from console"""
        return True


def parse(arg):
    """parse(arg):

        Description:
            Converts a series of strings to an argument tuple

        Return:
            Returns a tuple of arguments
    """
    return tuple(arg.split())


_built_in_classes = ['BaseModel', 'User', 'State', 'City',
                     'Amenity', 'Place', 'Review']


def parse_json_to_class_object(json_obj):
    """parse_json_to_class_obj(json_obj):

        Description:
            Parses a json object into a class object based on the json
            object's key: '__class__'.

        Return:
            Returns an object of specific built in class
    """
    # built_in_classes = ['BaseModel', 'User', 'State', 'City',
    #                     'Amenity', 'Place', 'Review']
    class_name = json_obj['__class__']
    if class_name in _built_in_classes:
        if class_name == 'BaseModel':
            return BaseModel(**json_obj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
