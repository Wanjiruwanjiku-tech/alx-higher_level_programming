#!/usr/bin/python3
"""
The script prints lists all state objects
that contain the letter 'a'
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':

    """
    Access the Database to get the states
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.contains('a'))

    if states is not None:
        for state in states:
            print('{0}: {1}'.format(state.id, state.name))
