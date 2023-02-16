#!/usr/bin/python3
""" Unit test for Review """
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """ Tests instance and methods from Class user """

    r1 = Review()

    def test_class_if_exists(self):
        """ tests if a class do exist """
        self.assertEqual(str(type(self.r1)), "<class 'models.review.Review'>")

    def test_if_inherits(self):
        """ tests if the user inherits from the BaseModel """
        self.assertIsInstance(self.r1, Review)

    def test_if_has_attributes(self):
        """ method checks if class has all the attributes """
        self.assertTrue(hasattr(self.r1, 'id'))
        self.assertTrue(hasattr(self.r1, 'updated_at'))
        self.assertTrue(hasattr(self.r1, 'created_at'))
        self.assertTrue(hasattr(self.r1, 'user_id'))
        self.assertTrue(hasattr(self.r1, 'place_id'))
        self.assertTrue(hasattr(self.r1, 'text'))

    def test_ifHas_attributes(self):
        """ this class tests if user has the attributes and is correct """
        self.assertIsInstance(self.r1.id, str)
        self.assertIsInstance(self.r1.updated_at, datetime.datetime)
        self.assertIsInstance(self.r1.created_at, datetime.datetime)
        self.assertIsInstance(self.r1.user_id, str)
        self.assertIsInstance(self.r1.place_id, str)
        self.assertIsInstance(self.r1.text, str)


if __name__ == '__main__':
    unittest.main()
