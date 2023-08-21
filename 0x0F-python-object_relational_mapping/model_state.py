#!/usr/bin/python3
"""
The script defines the Base and State classes
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base


class State(Base):
    """
    Code to be executed for the class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
