#!/usr/bin/python3
""" Unit test for State """
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """ Tests instance and methods from Class user """

    s1 = State()

    def test_class_if_exists(self):
        """ tests if a class state do exist """
        self.assertEqual(str(type(self.s1)), "<class 'models.state.State'>")

    def test_if_inherits(self):
        """ tests if the state inherits from the BaseModel """
        self.assertIsInstance(self.s1, State)

    def test_if_has_attributes(self):
        """ method checks if class state has all the attributes """
        self.assertTrue(hasattr(self.s1, 'id'))
        self.assertTrue(hasattr(self.s1, 'name'))
        self.assertTrue(hasattr(self.s1, 'created_at'))
        self.assertTrue(hasattr(self.s1, 'updated_at'))

    def test_ifHas_attributes(self):
        """ this class tests if user has the attributes and is correct """
        self.asserIsInstance(self.s1.id, str)
        self.asserIsInstance(self.s1.updated_at, str)
        self.asserIsInstance(self.s1.created_at, str)
        self.asserIsInstance(self.s1.name, str)


if __name__ == '__main__':
    unittest.main()
