#!/usr/bin/python3
"""This script defines the State class."""

from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship, backref
import models
from os import environ


class State(BaseModel, Base):
    """Represents a state.
    
    Attributes:
        name (str): The name of the state.
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if environ.get('HBNB_TYPE_STORAGE') == "db":
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete, delete-orphan")
    else:

        @property
        def cities(self):
            """Returns the list of City instances with state_id == current State.id."""
            all_cities = models.storage.all(City)
            state_cities = []
            for city_ins in all_cities.values():
                if city_ins.state_id == self.id:
                    state_cities.append(city_ins)

            return state_cities
