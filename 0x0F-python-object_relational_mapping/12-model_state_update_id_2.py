#!/usr/bin/python3
"""
the module runs a script that changes the name of a state
the script must use sqlalchemy
the script changes name of state where id = 2 to new mexico
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

def change_state_name(usename, password, database):
    """
    The function takes three parameters
    username = mysql username,
    password = mysql password
    and
    database = mysql database to use
    """
    # Create connection to the MySQL server
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(username, password, database))
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    # Make updates to the table and commit the changes to the database
    state_to_change = session.query(State).filter(State.id == 2).first()
    if state_to_change:
        state_to_change.name = 'New Mexico'
        session.commit()
    session.close()

if __name__ == "__main__":
    username, password, database = sys.argv[1:]
    change_state_name(username, password, database)