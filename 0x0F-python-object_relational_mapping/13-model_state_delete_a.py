#!/usr/bin/python3
"""
The module runs a script that deletes all state objects from a database
the module must use sqlalchemy
the Base and State classes must be imported from model_state
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username, password, database = sys.argv[1:]

    # create a connection to the mysql server
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(username, password, database))
    #create a session to interact with the databse
    Session = sessionmaker(bind=engine)
    session = Session()
    # find the state objects to delete
    states_to_delete = session.query(State).filter(State.name.ilike('%a%')).all()
    #delete the states
    for state in states_to_delete:
        session.delete(state)
    session.commit()
    session.close()

