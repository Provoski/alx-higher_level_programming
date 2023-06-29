#!/usr/bin/python3
"""8-model_state_fetch_first"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """
    fetch the firt state name and id form the dataabase.
    order by state id
    """

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(usr, pwd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id.asc()).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()
