#!/usr/bin/python3
""" Unittest for the file storage py file """
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestStorageInstance(unittest.TestCase):
    """ Unittest for the instances for the file storage """

    def testFile_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_private(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFile_With_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__object))

    def test_storage_init(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileMethods(unittest.TestCase):
    """ Unittest to test methods in the file storage """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)


def test_new(self):
    mod = BaseModel()
    u = User()
    s = State()
    p = Place()
    c = City()
    a = Amenity()
    r = Review()
    models.storage.new(mod)
    models.storage.new(u)
    models.storage.new(s)
    models.storage.new(p)
    models.storage.new(c)
    models.storage.new(a)
    models.storage.new(r)
    self.assertIn("BaseModel." + mod.id, models.storage.all().keys())
    self.assertIn(mod, models.storage.all().values())
    self.assertIn("User." + u.id, models.storage.all().keys())
    self.assertIn(u, models.storage.all().values())
    self.assertIn("State." + s.id, models.storage.all().keys())
    self.assertIn(s, models.storage.all().values)
    self.assertIn("Place." + p.id, models.storage.all().keys())
    self.assertIn(p, models.storage.all().values())
    self.assertIn("City." + c.id, models.storage.all().keys())
    self.assertIn(c, models.storage.all().values())
    self.assertIn("Review." + r.id, models.storage.all().keys())
    self.assertIn(r, models.storage.all().values())
    self.assertIn("Amenity." + a.id, models.storage.all().keys())
    self.assertIn(a, models.storage.all().values())


def test_new_args(self):
    with self.assertRaises(TypeError):
        models.storage.new(Basemodel(), 1)


def test_new_none(self):
    with self.assertRaises(AttributeError):
        models.storage.new(None)


if __name__ == "__main__":
    unittest.main()
