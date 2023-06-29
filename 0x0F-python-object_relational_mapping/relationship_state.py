#!/usr/bin/python3
"""model_state module"""
import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import City


Base = declarative_base()


class State(Base):
    """
    creates states table with column; id and name
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City",
            cascade='all, delete, delete-orphan',
            backref=backref("state", cascade="all")
            )

    def __init__(self, name):
        self.__name = name


if __name__ == '__main__':
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(user, pwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)
