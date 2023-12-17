#!/usr/bin/python3
"""
a script that deletes all State objects with a name containing the
letter a from the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
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

    """ Delete table """
    obj = session.query(State).filter(State.name.like('%a%')).all()

    for row in obj:
        session.delete(row)
    session.commit()
