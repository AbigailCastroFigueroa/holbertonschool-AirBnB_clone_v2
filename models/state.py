#!/usr/bin/python3
"""State Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """State class."""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete', backref='states')

    else:
        @property
        def cities(self):
            """Return cities that have the same state."""
            from models import storage
            new_list = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.__dict__['state_id'] == self.id:
                    new_list.append(city)
            return new_list
