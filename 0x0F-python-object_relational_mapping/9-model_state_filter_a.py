#!/usr/bin/python3
"""
The Module runs a script that listas all state objects that contain the letter 'a'
The module must use sqlalchemy
State and Base classes must be imported from model_state
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def filter_states(username, password, database):
    """
    The function takes three args namely:
    username = mysql username
    password = mysql password
    database = the specified database
    """
    # Create a connection to the mysql server
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(username, password, database))

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State and find all with 'a'
    states =  session.query(State).order_by(State.id).filter(State.name.ilike('%a%')).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    
    # Close Connection
    session.close()

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    filter_states(username, password, database)
