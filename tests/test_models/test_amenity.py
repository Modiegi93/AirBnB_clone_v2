#!/usr/bin/python3
""" module for testing Amenity class """
import unittest
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel
import os


class TestAmenity(unittest.TestCase):
    """ a class for testing Amenity"""

    @classmethod
    def setUpClass(cls):
        """ Example Data """
        cls.amen = Amenity()
        cls.amen.name = "Wifi"

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """ check for PEP8 style """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["models/amenity.py"])
        self.assertEqual(result.total_errors, 0, 'Fix PEP8')

    def test_docs(self):
        """ check for docstring """
        self.assertIsNotNone(Amenity.__doc__)

    def test_attribute_types(self):
        """ test Amenity attribute types """
        self.assertEqual(type(self.amen.name), str)

    def test_is_subclass(self):
        """ test if Amenity is subclass of BaseModel """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_save(self):
        """ test save() command """
        self.amen.save()
        self.assertNotEqual(self.amen.created_at, self.amen.updated_at)

    def test_sa_instance_state(self):
        """ test is _sa_instance_state has been removed """
        amen_dict = self.amen.to_dict()
        self.assertFalse("_sa_instance_state" in amen_dict.keys())


if __name__ == "__main__":
    unittest.main()
