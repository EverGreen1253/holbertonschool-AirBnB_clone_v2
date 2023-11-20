#!/usr/bin/python3
""" Amenity Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Table


class Amenity(BaseModel, Base):
    """ Review class to store review information """
    storage_engine = getenv('HBNB_TYPE_STORAGE')
    if storage_engine is None:
        storage_engine = "db"

    if storage_engine == "db":
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity_table, back_populates="amenities")
    else:
        name = ""
