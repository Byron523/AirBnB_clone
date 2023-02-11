#!/usr/bin/python3
""" A BaseModel class that defines common attributes/methods """
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ A BaseModel class that defines common attributes/methods """

    form = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """ An init method that instantiates files """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.__dict__['created_at'] = datetime.strptime(
                             kwargs.get('created_at'), self.form)
                elif 'updated_at' == key:
                    self.__dict__['updated_at'] = datetime.strptime(
                             kwargs.get('updated_at'), self.form)
                elif '__class__' == key:
                    pass
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """ This method prints dict, id and class """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the updated_at instance """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Return dicts containing keys/values """
        our_dict = {}

        our_dict = self.__dict__
        our_dict['__class__'] = type(self).__name__
        our_dict['created_at'] = our_dict['created_at'].strftime(self.form)
        our_dict['updated_at'] = our_dict['updated_at'].strftime(self.form)

        return (our_dict)
