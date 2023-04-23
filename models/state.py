#!/usr/bin/python3
"""
    Implementation of the State class
"""
import models
from models import storage
from models.base_model import BaseModel, Base
from models.city import City
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """Implementation for the State."""
    __tablename__ = 'states'

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes state"""
        super().__init__(*args, **kwargs)

    if models.storage_type != 'db':
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
