#!/usr/bin/python3
""" A BaseModel class that defines common attributes/methods """
import uuid
from datetime import datetime


class BaseModel:
    """ A BaseModel class that defines common attributes/methods """

    def __init__(self, *args, **kwargs):
        """ An init method that instantiates files """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            form = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(kwargs[key], form)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """ This method prints dict, id and class """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

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
