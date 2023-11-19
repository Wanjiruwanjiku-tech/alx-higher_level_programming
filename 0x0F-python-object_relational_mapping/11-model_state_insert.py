#!/usr/python3
"""
This Module runs a Script that add the state object louisiana into a database
the script must use sqlalchemy
State and Base classes must be imported from model_base module
the script must print the new states.id after ctreation
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username, password, database = sys.argv[1:]
    #create engine (connection to mysql server)
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(username, password, database))
    #create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    #create the new object
    new_state = State(name='Louisiana')
    session.add(new_state)
    #commit changes to the database
    session.commit()
    #print the new state's id
    print("{}".format(new_state.id))
