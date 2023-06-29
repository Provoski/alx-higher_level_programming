#!/usr/bin/python3
"""9-model_state_filter_a"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """
    fetch state that has 'a' in it
    """

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(user, pwd, db), pool_pre_ping-True)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State)
    states = query.filter(State.name.like('%a%')).order_by(State.id.asc())
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
