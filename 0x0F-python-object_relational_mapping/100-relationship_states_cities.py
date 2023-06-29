#!/usr/bin/python3
"""7-model_state_fetch_all"""
import sys
from relationship_state import Base, State
from relationship_city import City
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

    california = State(name="California")
    san_franscisco = City(name="San Francisco")
    california.cities.append(san_franscisco)
    session.add()
    session.commit()

    session.close()
