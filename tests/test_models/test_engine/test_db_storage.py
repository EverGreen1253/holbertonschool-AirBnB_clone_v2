#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
import os


storage = DBStorage()

class test_dbStorage(unittest.TestCase):
    """ Class to test the db storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._DBStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._DBStorage__objects[key]
