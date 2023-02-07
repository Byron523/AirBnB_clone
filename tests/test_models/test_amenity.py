#!/usr/bin/python3
""" Unit test for Amenity """
import unittest
from models.amenity import Amenity
import datetime


class TestUser(unittest.TestCase):
    """ Tests instance and methods from Class Amenity """

    a = Amenity()

    def test_class_if_exists(self):
        """ tests if a class amenity do exist """
        self.assertEqual(str(type(self.a)), "<class 'models.amenity.Amenity'>")

    def test_if_inherits(self):
        """ tests if the amenity inherits from the BaseModel """
        self.assertIsInstance(self.a, Amenity)

    def test_if_has_attributes(self):
        """ method checks if class amenity has all the attributes """
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))

    def test_ifHas_attributes(self):
        """ this class tests if amenity has the attributes and is correct """
        self.asserIsInstance(self.a.id, str)
        self.asserIsInstance(self.a.updated_at, datetime.datetime)
        self.asserIsInstance(self.a.created_at, datetime.datetime)
        self.asserIsInstance(self.a.name, str)


if __name__ == '__main__':
    unittest.main()
