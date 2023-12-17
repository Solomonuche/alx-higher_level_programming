#!/usr/bin/python3
"""
a script that adds the State object “Louisiana” to the database
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

    """ Create a new row/instance and commit """
    new_instance = State(name='Louisiana')

    session.add(new_instance)
    session.commit()

    """ print new instance id """
    obj = session.query(State).filter(State.name == 'Louisiana').first()

    print(obj.id)
