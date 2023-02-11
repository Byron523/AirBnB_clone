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
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ Save serializes the JSON fie """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            our_d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(our_d, f)

    def classes(self):
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

        return (our_dict)

    def reload(self):
        """ Reloads stored objects """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            o_d = json.load(f)
            o_d = {k: self.classes()[v["__class__"]](**v)
                   for k, v in o_d.items()}
            FileStorage.__objects = o_d

    def attributes(self):
        """ Returns attributes and types """
        attr = {
          "BaseModel":
                   {"id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime},
          "User":
                   {"email": str,
                    "password": str,
                    "first_name": str,
                    "last_name": str},
          "State":
                   {"name": str},
          "City":
                   {"state_id": str,
                    "name": str},
          "Amenity":
                   {"name": str},
          "Place":
                   {"city_id": str,
                    "user_id": str,
                    "name": str,
                    "description": str,
                    "number_rooms": int,
                    "number_bathrooms": int,
                    "max_guest": int,
                    "price_by_night": int,
                    "latitude": float,
                    "longitude": float,
                    "amenity_ids": list},
          "Review":
                   {"place_id": str,
                    "user_id": str,
                    "text": str}
        }
        return attrr
