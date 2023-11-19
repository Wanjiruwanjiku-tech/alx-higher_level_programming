#!/usr/bin/python3
"""
The module runs a script that lists all states from a database
The Module uses SQLAlchemy
Base and State must be imported from model_state
Results must be stored in asc order by states.id
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create a connection to the MySQL server
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(username, password, database))

    # Create a Session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querry all state objects and display the result
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the Session
    session.close   

