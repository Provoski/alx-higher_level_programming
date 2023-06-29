#!/usr/bin/python3
"""13-model_state_delete_a"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """
    delete state object that has 'a' in is name
    """

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(user, pwd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)
    session.commit()

    session.close()
