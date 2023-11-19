#!/usr/bin/python3
"""
This Module runs a script that contains a class definition
of a State and an instance of Base =declarative_base
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """The class links to the MySQL table states"""
    # Define the table Structure
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,autoincrement=True)
    name = Column(String(128), nullable=False)

# Connect to a server running on localhost on port 3306
#engine = create_engine('mysql://username:password@localhost:3306/database')

# Create the table
#Base.metadata.create_all(engine)
# Create the session
#Session = sessionmaker(bind=engine)
#session = Session()
