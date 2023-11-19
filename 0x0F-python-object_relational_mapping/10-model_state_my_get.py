#!/usr/bin/python
"""
The Module runs a script that prints the state object with the name passes as arg
The script must use SQLAlchemy
State and Base classes must be imported from model_state
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_state(username, password, database, stateName):
    """
    The Function takes 4 parameters;
    username = mysql username,
    password = mysql password,
    database = mysql database,
    stateName =  the name to be searched.
    """
    engine = create_engine('mysql://{}:{}@localhost:3306/{}')
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name == stateName).first()
    if states:
        print(states.id)
    else:
        print("Not found")
    
    session.close
if __name__ == "__main__":
    username, password, database, stateName = sys.argv[1:]
    get_state(username, password, database, stateName)