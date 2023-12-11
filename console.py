#!/usr/bin/env python3
"""This is the console"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """This class defines the console"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")  # Print a new line before exiting
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
