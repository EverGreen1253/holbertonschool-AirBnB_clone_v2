#!/usr/bin/python3
""" Review module for the HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review class to store review information """
    storage_engine = getenv('HBNB_TYPE_STORAGE')
    if storage_engine is None:
        storage_engine = "db"

    if storage_engine == "db":
        __tablename__ = 'reviews'

        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'),
                          nullable=False, default="")
        user_id = Column(String(60), ForeignKey('users.id'),
                         nullable=False, default="")
        user = relationship("User", back_populates="reviews")
        place = relationship("Place", back_populates="reviews")
    else:
        text = ""
        place_id = ""
        user_id = ""
