#!/usr/bin/python3
"""
This module runs a scriptt that prints the first State from the database
The script must use SQLAlchemy
State and Base classes must be imported from model_state module
The state displayed must be first in state.id
You are not allowed to fetch all before displaying the result
If the table states is empty, print nothing followed by a new line
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ =="__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create a connection to MySQL server
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(username, password, database))

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querry state objects and display the first result
    firstState= session.query(State).order_by(State.id).first()
    if firstState:
        print("{}: {}".format(firstState.id, firstState.name))
    else:
        print("\n")
    
    # Close the session
    session.close()