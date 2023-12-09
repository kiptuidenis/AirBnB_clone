#!/usr/bin/env python3
"""This is the console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines the console"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")  # Print a new line before exiting
        return True

    def emptyline(self):
        """Handle empty line """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
