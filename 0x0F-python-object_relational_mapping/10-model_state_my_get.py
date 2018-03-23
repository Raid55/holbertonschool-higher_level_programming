#!/usr/bin/python3
""" querys db for states id that matches argv """
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    sesh = Session()

    tmp = sesh.query(State).filter(State.name == sys.argv[4])

    if tmp.count():
        print(tmp[0].id)
    else:
        print('Not found')

    sesh.close()
