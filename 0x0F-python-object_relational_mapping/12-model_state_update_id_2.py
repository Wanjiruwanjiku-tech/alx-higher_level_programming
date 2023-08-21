#!/usr/bin/python3
"""
The script changes the name of
a state object
'louisiana'
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

    state = session.query(State).filter(state.id == 2).first
    state.name = "New Mexico"
    session.commit()

    session.close
