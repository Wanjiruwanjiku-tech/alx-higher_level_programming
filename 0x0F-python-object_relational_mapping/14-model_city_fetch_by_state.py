#!/usr/bin/python3
"""
The script prints all city objects
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':

    """
    Access the Database to get the cities
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    
    session = Session()

    results = session.query(City, State).join(State)

    for city, state in results.all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    
    session.commit()

    session.close
