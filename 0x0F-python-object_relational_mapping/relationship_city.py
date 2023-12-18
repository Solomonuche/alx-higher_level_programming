#!/usr/bin/python3
"""
a python file that contains the class definition of a city and
an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
    City class representation that inherits from class and mapp to a database
    """

    __tablename__ = "cities"

    id = Column(Integer, nullable=False, autoincrement=True,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Relationship
    state = relationship('State', back_populates='cities')
