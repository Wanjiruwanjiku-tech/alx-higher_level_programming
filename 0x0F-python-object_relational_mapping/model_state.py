#!/usr/bin/python3
"""
The script defines the Base and State classes
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    Code to be executed for the class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

if __name__ == '__main__':
    """ Create Engine """
    engine = create_engine("mysql+pymysql://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))

    Base.metadata.create_all(engine)

