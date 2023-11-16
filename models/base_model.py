#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime


Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            values = kwargs.copy()

            if 'id' not in values:
                values['id'] = str(uuid.uuid4())

            if 'updated_at' not in values:
                values['updated_at'] = datetime.now()
            else:
                values['updated_at'] = datetime.strptime(values['updated_at'],
                                                         '%Y-%m-%dT%H:%M:%S.%f')

            if 'created_at' not in values:
                values['created_at'] = datetime.now()
            else:
                values['created_at'] = datetime.strptime(values['created_at'],
                                                         '%Y-%m-%dT%H:%M:%S.%f')

            if '__class__' in values:
                del values['__class__']

            self.__dict__.update(values)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models.__init__ import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}

        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        if "_sa_instance_state" in dictionary:
            dictionary.pop("_sa_instance_state")

        return dictionary

    def delete(self):
        """Removes current instance reference from within objects and saves it
        """
        from models.__init__ import storage
        storage.delete(self)
        storage.save()
