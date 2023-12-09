#!/usr/bin/env python3
"""This is the console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines the console"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quits the cmd interpreter"""
        return True

    def do_EOF(self, args):
        """End of File"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
