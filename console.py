#!/usr/bin/python3
"""AirBnB Console Module
"""
import sys
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
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
        if argv is None or len(argv) < 1:
            print("** class name missing **")
            return
        if not (argv[0] in _built_in_classes):
            print("** class doesn't exist **")
            return
        obj = create_class(argv[0])
        print(obj.id)
        obj.save()

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
        if argv is None or len(argv) < 1:
            print("** class name missing **")
            return
        if not (argv[0] in _built_in_classes):
            print("** class doesn't exist **")
            return
        if (len(argv) < 2):
            print("** instance id missing **")
            return
        key = "{}.{}".format(argv[0], argv[1])
        if not (key in storage.all()):
            print("** no instance found **")
            return
        obj = create_class(argv[0], **(storage.all()[key]))
        print(str(obj))

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
        if argv is None or len(argv) < 1:
            print("** class name missing **")
            return
        if not (argv[0] in _built_in_classes):
            print("** class doesn't exist **")
            return
        if (len(argv) < 2):
            print("** instance id missing **")
            return
        key = "{}.{}".format(argv[0], argv[1])
        if not (key in storage.all()):
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

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
        if argv is None or len(argv) < 1:
            print(list(map(get_str, storage.all().values())))
            return
        if not (argv[0] in _built_in_classes):
            print("** class doesn't exist **")
            return
        objs = storage.all().values()
        objs = list(filter(lambda o: o['__class__'] == argv[0], objs))
        objs = list(map(get_str, objs))
        print(objs)

    def do_update(self, arg):
        """update(arg):

            Description:
                Updates a field of an object.

            Args:
                arg: <class name> <id> <attribute name> "<attribute value>"

            Implementation:
            $ update <class name> <obj id> <attribute name> <attribute value>
            $ update User fe15e5e2d6e2d6e2de6d6ed first_name Allen

        """
        argv = parse(arg)
        if argv is None:
            print("** class name missing **")
            return
        argc = len(argv)
        if not (argv[0] in _built_in_classes):
            print("** class doesn't exist **")
            return
        if argc < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(argv[0], argv[1])
        if not (key in storage.all().keys()):
            print("** no instance found **")
            return
        if argc < 3:
            print("** attribute name missing **")
            return
        if argc < 4:
            print("** value missing **")
            return
        json_obj = storage.all()[key]
        json_obj[argv[2]] = str(argv[3].split('" ', 1)[0].replace('"', ''))
        storage.save()

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
    # element = tuple(arg.split(' ',3))
    # print(element)
    if arg == "":
        return None
    return tuple(arg.split(' ', 4))


_built_in_classes = ['BaseModel', 'User', 'State', 'City',
                     'Amenity', 'Place', 'Review']


def create_class(class_name, **kwargs):
    """create_class(class_name, **kwargs)

        Description:
            Creates a class object give a class name. Passes attributes
            to class if available.

        Args:
            class_name: Name of the class
            **kwargs: A dictionary of the class bearing its attributes

        Returns:
            Returns an object of specified class

        Class List:
            [BaseModel, User, State, City, Amenity, Place, Review]
    """
    if not (class_name in _built_in_classes):
        return None
    if class_name == 'BaseModel':
        return BaseModel(**kwargs)
    if class_name == 'User':
        return User(**kwargs)
    if class_name == 'State':
        return State(**kwargs)
    if class_name == 'City':
        return City(**kwargs)
    if class_name == 'Amenity':
        return Amenity(**kwargs)
    if class_name == 'Place':
        return Place(**kwargs)
    if class_name == 'Review':
        return Review(**kwargs)
    


def parse_json_to_class_object(json_obj):
    """parse_json_to_class_obj(json_obj):

        Description:
            Parses a json object into a class object based on the json
            object's key: '__class__'.

        Return:
            Returns an object of specific built in class
    """
    class_name = json_obj['__class__']
    if not (class_name in _built_in_classes):
        return None
    obj = create_class(class_name, **json_obj)
    return obj


if __name__ == '__main__':
    HBNBCommand().cmdloop()
