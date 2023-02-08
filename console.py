#!/usr/bin/python3
""" A Python interpreter (shell like) """
import cmd, sys
import json
import shlex


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to HBNB Console'
    prompt = '(hbnb) '

    my_ex = ['byron', 'gumbo', 'munyaradzi', 'student']
    acc = ['electronic', 'maths', 'ecs', 'geo']

    def do_create(self, line):
        """ Creates a new instance of BaseModel """

    def do_EOF(self, line):
        "Exit"
        return True

    def do_quit(self, line):
        "Quit command to exit the interpreter"
        return True

    def emptyline(self):
        """ Do nothing when empty line is passed """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
