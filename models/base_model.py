#!/usr/bin/python3
""" A BaseModel class that defines common attributes/methods """
import uuid
from datetime import datetime


class BaseModel:
    """ A BaseModel class that defines common attributes/methods """

    def __init__(self):
        """ An init method that instantiates files """
        self.id = str(uuid.uuid4)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ This method prints dict, id and class """

    def save(self):
        """ Updates the updated_at instance """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Return dicts containing keys/values """
        our_dict = {}

        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                our_dict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not value:
                    pass
                else:
                    our_dict[key] = value

        our_dict['__class__'] = self.__class__.__name__

        return (our_dict)
