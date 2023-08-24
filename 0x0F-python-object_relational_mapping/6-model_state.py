#!/usr/bin/python3
"""
The Script defines a class state and a base
class to work with SQLAlchemy
"""

from sqlalchemy import (create_engine)
from model_state import Base, State
import sys

if __name__ == '__main__':
    """
    Create Engine
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
