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
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ Save serializes the JSON fie """
        our_dict = {}

        for key, value in FileStorage.__objects.items():
            our_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(our_dict, f)

    def reload(self):
        """  Deserializes the JSON file to __objects """
