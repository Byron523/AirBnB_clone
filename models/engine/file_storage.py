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
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        from models.state import State
        from models.user import User

        our_dict = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'City': City, 'Amenity': Amenity, 'State': State,
                    'Review': Review}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as fil:
                for key, value in json.load(fil).items():
                    self.new(our_dict[value['__class__']](**value))
