#!/usr/bin/python3
""" inserts Lou back into isiana """
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    sesh = Session()
    
    newState = State(name="Louisiana")
    tmp = sesh.add(newState)
    sesh.commit()

    print(sesh.query(State).filter(State.name == "Louisiana")[0].id)

    sesh.close()
