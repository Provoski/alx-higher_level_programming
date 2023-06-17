#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
"""
model_state module
"""


Base = declarative_base()


class State(Base):
    """
    creates states table with column; id and name
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(1280), nullable=False)


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(username, password, db))

    Base.metadata.create_all(engine)
