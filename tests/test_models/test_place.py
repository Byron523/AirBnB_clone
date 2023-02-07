#!/usr/bin/python3
""" Unit test for Place """
import unittest
from models.place import Place


class TestUser(unittest.TestCase):
    """ Tests instance and methods from Class Place """

    p1 = Place()

    def test_class_if_exists(self):
        """ tests if a class Place do exist """
        self.assertEqual(str(type(self.p1)), "<class 'models.place.Place'>")

    def test_if_inherits(self):
        """ tests if the Place inherits from the BaseModel """
        self.assertIsInstance(self.p1, Place)

    def test_if_has_attributes(self):
        """ method checks if class Place has all the attributes """
        self.assertTrue(hasattr(self.p1, 'id'))
        self.assertTrue(hasattr(self.p1, 'city_id'))
        self.assertTrue(hasattr(self.p1, 'user_id'))
        self.assertTrue(hasattr(self.p1, 'name'))
        self.assertTrue(hasattr(self.p1, 'description'))
        self.assertTrue(hasattr(self.p1, 'number_room'))
        self.assertTrue(hasattr(self.p1, 'number_bathrooms'))
        self.assertTrue(hasattr(self.p1, 'max_guest'))
        self.assertTrue(hasattr(self.p1, 'price_by_night'))
        self.assertTrue(hasattr(self.p1, 'latitude'))
        self.assertTrue(hasattr(self.p1, 'longitude'))
        self.assertTrue(hasattr(self.p1, 'amenity_ids'))

    def test_ifHas_attributes(self):
        """ this class tests if user has the attributes and is correct """
        self.asserIsInstance(self.p1.city_id, str)
        self.asserIsInstance(self.p1.user_id, str)
        self.asserIsInstance(self.p1.name, str)
        self.asserIsInstance(self.p1.description, str)
        self.asserIsInstance(self.p1.number_room, int)
        self.asserIsInstance(self.p1.number_bathrooms, int)
        self.asserIsInstance(self.p1.max_guest, int)
        self.asserIsInstance(self.p1.price_by_night, int)
        self.asserIsInstance(self.p1.latitude, float)
        self.asserIsInstance(self.p1.longitude, float)
        self.asserIsInstance(self.p1.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
