#!/usr/bin/python3
""" updates row with id 2 """
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    sesh = Session()
    
    sesh.query(State).filter_by(id=2).update({"name": "New Mexico"})
    sesh.commit()

    sesh.close()
