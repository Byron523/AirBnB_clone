#!/usr/bin/python3
""" base module unittests """
import unittests
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage
import datetime


class BaseModelsTests(unittest.TestCase):
    """ Base model tests """

    base = BaseModel()

    def testBase(self):
        """ testing for the value of Basemodel """

        self.base.name = "ALX"
        self.base.my_number = 89
        self.base.save()
        bas_json = self.base.to_dict()

        self.assertEqual(self.base.name, base_json['name'])
        self.assertEqual(self.base.my_number, base_json['my_number'])
        self.assertEqual('BaseModel', base_json['__clas__'])
        self.assertEqual(self.base.id, base_json['id'])

    def test_save_method(self):
        """ Checking if save method to works """
        self.base.first_name = "Naumi"
        self.base.save()

        self.assertIsInstance(self.base.id, str)
        self.assertIsInstance(self.base.created_at, datetime.datetime)
        self.assertIsInstance(self.base.updated_at, datetime.datetime)

        f_d = self.base.to_dict()

        self.base.first_name = "Second"
        self.base.save()
        s_d = self.base.to_dict()

        self.assertEqual(f_d['created_at'], s_d['created_at'])
        self.assertNotEqual(f_d['updated_at'], s_d['updated_at'])


if __name__ == '__main__':
    unittest.main()
