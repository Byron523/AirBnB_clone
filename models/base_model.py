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
        #TODO

    def save(self):
        """ Updates the updated_at instance """
        #TODO

    def to_dict(self):
        """ Return dicts containing keys/values """
        #TODO