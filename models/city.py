#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """Class to declare the cities database table
    """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey(State.id), nullable=False)
    state = relationship("State", back_populates="cities")
