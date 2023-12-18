#!/usr/bin/python3
"""
a python file that contains the class definition of a State and
an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    State class representation that inherits from class and mapp to a database
    """

    __tablename__ = "states"

    id = Column(Integer, nullable=False, autoincrement=True,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)

    # Relatioship
    cities = relationship('City', back_populates='state')
