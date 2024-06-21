#!/usr/bin/python3
"""Nameless module to suck data out from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = sys.argv[4]

    query = session.query(State).where(State.name == state_name)

    if query.count() == 0:
        print("Not found")
    else:
        row = query.limit(1).one()
        print("{0}".format(row.id))
