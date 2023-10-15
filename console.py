#!/usr/bin/python3
"""AirBnB Console Module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class: Command line shell interpreter interface for
        testing.
    """
    intro = ''
    prompt = '(hbnb)'

    def emptyline(self):
        """On empty line, do nothing"""
        pass

    def do_EOF(self, line):
        """Exit on 'end of line' from console"""
        return True

    def do_quit(self, line):
        """Exit from console"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
