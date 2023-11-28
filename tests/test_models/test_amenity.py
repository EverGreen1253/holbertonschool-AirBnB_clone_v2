#!/usr/bin/python3
""" """
import json
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.__init__ import storage
from os import getenv


storage_engine = getenv('HBNB_TYPE_STORAGE')

class test_Amenity(test_basemodel):
    """ Class for testing Amenity """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        attribs = {"name":"Toilet"}
        new = self.value(**attribs)
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(storage_engine == "fs", "not using DBStorage")
    def test_db_save(self):
        """ Testing DB save """
        attribs = {"name":"Wifi"}
        i = self.value(**attribs)
        i.save()
        am = storage.all(self.value)
        self.assertTrue(len(am) > 0)

    def test_amenity_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.to_dict()))
