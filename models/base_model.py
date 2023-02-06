#!/usr/bin/python3
""" A BaseModel class that defines common attributes/methods """
import uuid
from datetime import datetime

class BaseModel:
    """ A BaseModel class that defines common attributes/methods """

    def __init__(self):
        """ An init method that instantiates files """
        self.id = str(uuid.uuid4)
