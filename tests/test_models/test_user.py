#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    attribs = {
        "first_name":"Clark",
        "last_name": "Kent",
        "email":"test@email.com",
        "password": "abc123"
    }

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value(**self.attribs)
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value(**self.attribs)
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value(**self.attribs)
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value(**self.attribs)
        self.assertEqual(type(new.password), str)

    def test_user_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.to_dict()))
