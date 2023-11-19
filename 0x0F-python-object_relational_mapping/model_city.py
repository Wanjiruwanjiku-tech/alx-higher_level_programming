#!/usr/bin/python3
"""
This module inherits from base which is imported from model_state
* class attribute id reps a column of autogenerated, unique integers
* class attribute name reps a column of a string of 128 chars and cant be null
* class attribute state_id reps a column of an integer,cant be null and is a foreignkey to states.id
The module must use sqlalchemy
"""
from model_state import Base, State
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")
