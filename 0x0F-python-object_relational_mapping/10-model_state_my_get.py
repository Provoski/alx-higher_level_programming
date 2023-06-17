#!/usr/bin/python3
"""10-model_state_my_get"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """
    fetch state where state name is
    equal to passed state name argument
    """

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(user, pwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    S = State
    qry = session.query(S)
    states = qry.filter(S.name == state_name).order_by(S.id.asc()).first()

    if states:
        print("{}".format(states.id))
    else:
        print("Not found")

    session.close()
