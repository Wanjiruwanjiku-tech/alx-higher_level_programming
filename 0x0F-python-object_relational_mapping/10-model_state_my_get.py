#!/usr/bin/python3
"""
The script prints the first state objects
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

    state = session.query(State).filter(State.name == argv[4].first())

    if state is not None:
        print('{0}'.format(state.id))
    else:
        print("Not found")
