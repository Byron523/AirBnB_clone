#!/usr/bin/python3
""" A Python interpreter (shell like) """
import cmd, sys


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to HBNB Console'
    prompt = '(hbnb) '

    def do_EOF(self, line):
        "Exit"
        return True

    def do_quit(self):
        "Quit command to exit the program"
        os._exit(1)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
