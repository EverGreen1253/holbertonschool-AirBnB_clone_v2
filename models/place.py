#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Null, Table


if getenv('HBNB_TYPE_STORAGE') is None or getenv('HBNB_TYPE_STORAGE') == "db":
    place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'), nullable=False, primary_key=True),
        Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False, primary_key=True),
        extend_existing=True
    )

class Place(BaseModel, Base):
    """ A place to stay """
    storage_engine = getenv('HBNB_TYPE_STORAGE')
    if storage_engine is None:
        storage_engine = "db"

    if storage_engine == "db":
        __tablename__ = 'places'

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True, default=Null())
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True, default=Null())
        longitude = Column(Float, nullable=True, default=Null())
        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship("Review", back_populates="place", cascade="delete, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """FileStorage Getter that returns

                Returns:
                    List of Reviews with place_id of current instance id
            """
            from models.__init__ import storage

            data = storage.all()
            filtered = []
            for k, v in data.items():
                if k.split('.')[0] == "Reviews" and self.id == v.id:
                    filtered.append(v)

            return filtered

        @property
        def amenities(self):
            """FileStorage Getter that returns

                Returns:
                    List of Amenities linked to this Place whose ids are in amenity_ids
            """
            from models.__init__ import storage

            data = storage.all()
            filtered = []
            for k, v in data.items():
                if k.split('.')[0] == "Amenities" and v.id in self.amenity_ids:
                    filtered.append(v)

            return filtered

        @amenities.setter
        def amenities(self, obj):
            """Appends to the ids list of amenities.

                Returns:
                    Nothing
            """

            if str(type(obj).__name__) == 'Amenity':
                self.amenity_ids.append(obj.id)
