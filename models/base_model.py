#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """A base class for all hbnb models"""

    id = None
    created_at = None
    updated_at = None

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            values = kwargs.copy()

            if 'id' not in values:
                values['id'] = str(uuid.uuid4())

            if 'updated_at' not in values:
                values['updated_at'] = datetime.now()
            else:
                values['updated_at'] = datetime.strptime(values['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

            if 'created_at' not in values:
                values['created_at'] = datetime.now()
            else:
                values['created_at'] = datetime.strptime(values['created_at'], '%Y-%m-%dT%H:%M:%S.%f')

            if '__class__' in values:
                del values['__class__']

            self.__dict__.update(values)
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
