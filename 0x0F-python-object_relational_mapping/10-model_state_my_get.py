#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    """states = session.query(State).filter(State.name.like(f'{sys.argv[4]}')).order_by(State.id.asc().all()"""
    rows = session.query(State).order_by(State.id.asc().count()
    if rows == 0:
        print("Not found")
    else:
        for state in states:
            print("{}".format(state.name))
    session.close()
