#!/usr/bin/python3
""" Unit test for Users """
import unittest
from models.user import User
import datetime


class TestUser(unittest.TestCase):
    """ Tests instance and methods from Class user """

    user1 = User()

    def test_class_if_exists(self):
        """ tests if a class do exist """
        self.assertEqual(str(type(self.user1)), "<class 'models.user.User'>")

    def test_if_inherits(self):
        """ tests if the user inherits from the BaseModel """
        self.assertIsInstance(self.user1, User)

    def test_if_has_attributes(self):
        """ method checks if class has all the attributes """
        self.assertTrue(hasattr(self.user1, 'id'))
        self.assertTrue(hasattr(self.user1, 'email'))
        self.assertTrue(hasattr(self.user1, 'password'))
        self.assertTrue(hasattr(self.user1, 'first_name'))
        self.assertTrue(hasattr(self.user1, 'last_name'))
        self.assertTrue(hasattr(self.user1, 'created_at'))
        self.assertTrue(hasattr(self.user1, 'updated_at'))

    def test_if_has_attributes(self):
        """ this class tests if user has the attributes and is correct """
        self.assertIsInstance(self.user1.first_name, str)
        self.assertIsInstance(self.user1.last_name, str)
        self.assertIsInstance(self.user1.email, str)
        self.assertIsInstance(self.user1.id, str)
        self.assertIsInstance(self.user1.password, str)
        self.assertIsInstance(self.user1.created_at, datetime.datetime)
        self.assertIsInstance(self.user1.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
