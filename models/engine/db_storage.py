#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import importlib
from os import getenv
from models.base_model import Base

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class is for DBStorage"""
    __engine = None
    __session = None
    __module_names = {
        "BaseModel": "base_model",
        "User": "user",
        "State": "state",
        "City": "city",
        "Amenity": "amenity",
        "Place": "place",
        "Review": "review"
    }

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True
        )

        if getenv('HBNB_MYSQL_DB)') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary of everything"""
        output = {}
        if self.__session is not None:
            if cls is not None:
                module = importlib.import_module("models." + self.__module_names[cls])
                class_ = getattr(module, cls)
                rows = self.__session.query(class_).all()

                for row in rows:
                    key = str(cls + "." + row.id)
                    output[key] = row.to_dict()
            else:
                for class_name, namespace in self.__module_names.items():
                    module = importlib.import_module("models." + namespace)
                    class_ = getattr(module, class_name)
                    rows = self.__session.query(class_).all()

                    for row in rows:
                        key = str(class_name + "." + row.id)
                        output[key] = row.to_dict()

        return output

    def new(self, obj):
        """Add new object to session"""
        if self.__session is not None and obj is not None:
            self.__session.add(obj)

    def save(self):
        """Commit changes for current session"""
        if self.__session is not None:
            self.__session.commit()

    def delete(self, obj=None):
        """Delete object from session"""
        if self.__session is not None:
            if obj is not None:
                self.__session.delete(obj)

    def reload(self):
        """Recreate everything"""
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()