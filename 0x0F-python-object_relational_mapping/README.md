PYTHON - OBJECT RELATIONAL MAPPERS.
----------------------------------------------

ORM is a code library that creates high level Abstraction by allowing developers to interact with Databases
by writing python code instead of SQL.

This project will Implement SQLAlchemy to interact with databases.

Dealing with SQLAlchemy.
-------------------------------------
1. Installation


    pip install sqlalchemy


2. Connecting to a database


    from sqlalchemy import create-engine
    engine = create_engine(<appropriate url to the database>)


3. Defining table structures.


    from sqlalchemy import Column, Integer, String, Sequence, create_engine
    from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()
    class User(Base):
        __tableName__ = 'Users'
        id = Column(Integer)
        name = Column(String(50))
        age = (Integer)


4. Creating the Table


    Base.metadata.create_all(engine)


5. Inserting Data.


    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    newUser = User(name='john doe', age=30)
    session.add(newUser)
    session.commit()


6. Querying Data.


    users = session.query(User).all()
        for user in users:
            print(user.name, user.age)

