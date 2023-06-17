#!/usr/bin/python3
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
"""14-model_city_fetch_by_state"""


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(username, password, db))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    qry = session.query(City)
    cities = qry.join(State).order_by(City.id.asc()).all()
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    session.close()
