#!/usr/bin/python3
"""
a script that changes the name of a State object from the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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
    obj = session.query(City).join(State, City.state_id == State.id).\
        order_by(City.id)

    for row in obj:
        print(f'{row.state.name}: ({row.id}) {row.name}')
