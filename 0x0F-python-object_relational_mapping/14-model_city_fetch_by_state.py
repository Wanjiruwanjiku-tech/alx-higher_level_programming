#!/usr/bin/python3
"""
The module prints all City objects from a specified database.
The module must use SQLAlchemy.
State and Base classes must be imported from model_state
Results must be sorted in ascending order by cities.id
Results are to be displayed in the format 'state name: city id city name'
The module takes 3 args
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username, password, database = sys.argv[1:]

    #create a connection
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(username, password, database))
    Base.metadata.create_all(engine)
    
    #create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    #get the list of all cities
    cities = session.query(City).join(State).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    session.close()
