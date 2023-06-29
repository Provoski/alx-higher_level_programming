#!/usr/bin/python3
"""12-model_state_update_id_2"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """
    change a state object name
    with id of 2 to 'New Mexico'
    """

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(user, pwd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()

    session.close()
