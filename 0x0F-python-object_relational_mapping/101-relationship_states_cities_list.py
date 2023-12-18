#!/usr/bin/python3
"""
a script that changes the name of a State object from the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    """connect to the server """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    """ Create session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Query with relationship """
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')

        for city in state.cities:
            print(f'    {city.id}: {city.name}')
