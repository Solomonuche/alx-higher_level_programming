#!/usr/bin/python3
"""
a script that lists all State objects that contain the letter a
from the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = sys.argv[4]
    obj = session.query(State).filter(State.name == state_name).\
        order_by(State.id).first()

    if obj:
        print(obj.id)
    else:
        print('Not found')
