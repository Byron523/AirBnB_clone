#!/usr/bin/python3
""" A File Storage Class """
import json
import os


class FileStorage:
    """ FileStorage Serializes instances to JSON file """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary """
        return (FileStorage.__objects)

    def new(self, obj):
        """ New sets objects with key
        Args:
            obj: the object file contains keys
        """

    def save(self):
        """ Save serializes the JSON fie """

    def reload(self):
        """  Deserializes the JSON file to __objects """