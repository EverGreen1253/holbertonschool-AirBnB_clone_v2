#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    storage_engine = getenv('HBNB_TYPE_STORAGE')
    if storage_engine is None:
        storage_engine = "db"

    if storage_engine == "db":
        __tablename__ = 'users'

        email = Column(String(128), nullable=False, default="")
        password = Column(String(128), nullable=False, default="")
        first_name = Column(String(128), nullable=False, default="")
        last_name = Column(String(128), nullable=False, default="")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
