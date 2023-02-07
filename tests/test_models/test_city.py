#!/usr/bin/python3
""" Unit test for City """
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """ Tests instance and methods from Class user """

    city1 = City()

    def test_class_if_exists(self):
        """ tests if a class do exist """
        self.assertEqual(str(type(self.city1)), "<class 'models.city.City'>")

    def test_if_inherits(self):
        """ tests if the city inherits from the BaseModel """
        self.assertIsInstance(self.city1, City)

    def test_if_has_attributes(self):
        """ method checks if class City has all the attributes """
        self.assertTrue(hasattr(self.city1, 'id'))
        self.assertTrue(hasattr(self.city1, 'state_id'))
        self.assertTrue(hasattr(self.city1, 'city_name'))
        self.assertTrue(hasattr(self.city1, 'created_at'))
        self.assertTrue(hasattr(self.city1, 'updated_at'))

    def test_ifHas_attributes(self):
        """ this class tests if City has the attributes and is correct """
        self.asserIsInstance(self.city1.id, str)
        self.asserIsInstance(self.city1.state_id, str)
        self.asserIsInstance(self.city1.city_name, str)
        self.asserIsInstance(self.city1.created_at, datetime.datetime)
        self.asserIsInstance(self.city1.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
