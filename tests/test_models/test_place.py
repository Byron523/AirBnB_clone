#!/usr/bin/python3
""" Unit test for Users """
import unittest
from models.place import Place
import datetime


class TestUser(unittest.TestCase):
    """ Tests instance and methods from Class Place """

    user1 = Place()

    def test_class_if_exists(self):
        """ tests if a class Place do exist """
        self.assertEqual(str(type(self.user1)), "<class 'models.user.User'>")

    def test_if_inherits(self):
        """ tests if the Place inherits from the BaseModel """
        self.assertIsInstance(self.user1, User)

    def test_if_has_attributes(self):
        """ method checks if class Place has all the attributes """
        self.assertTrue(hasattr(self.user1, 'id'))
        self.assertTrue(hasattr(self.user1, 'city_id'))
        self.assertTrue(hasattr(self.user1, 'user_id'))
        self.assertTrue(hasattr(self.user1, 'name'))
        self.assertTrue(hasattr(self.user1, 'description'))
        self.assertTrue(hasattr(self.user1, 'number_room'))
        self.assertTrue(hasattr(self.user1, 'number_bathrooms'))
        self.assertTrue(hasattr(self.user1, 'max_guest'))
        self.assertTrue(hasattr(self.user1, 'price_by_night'))
        self.assertTrue(hasattr(self.user1, 'latitude'))
        self.assertTrue(hasattr(self.user1, 'longitude'))
        self.assertTrue(hasattr(self.user1, 'amenity_ids'))

    def test_ifHas_attributes(self):
        """ this class tests if user has the attributes and is correct """
        self.asserisInstance(self.user1.city_id, str)
        self.asserisInstance(self.user1.user_id, str)
        self.asserisInstance(self.user1.name, str)
        self.asserisInstance(self.user1.description, str)
        self.asserisInstance(self.user1.number_room, int)
        self.asserisInstance(self.user1.number_bathrooms, int)
        self.asserisInstance(self.user1.max_guest, int)
        self.asserisInstance(self.user1.price_by_night, int)
        self.asserisInstance(self.user1.latitude, float)
        self.asserisInstance(self.user1.longitude, float)
        self.asserisInstance(self.user1.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
