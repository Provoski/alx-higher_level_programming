#!/usr/bin/python3
"""7-model_state_fetch_all"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """
    print all state ordered in ascending order of id
    """

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(user, pwd, db, pool_pre_ping=True))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id.asc())
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
