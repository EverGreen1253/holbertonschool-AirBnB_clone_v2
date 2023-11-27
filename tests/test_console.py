#!/usr/bin/python3
"""Module for testing console"""
import unittest
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class test_console(unittest.TestCase):
    """ Class to test the airbnb console """
