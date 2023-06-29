#!/usr/bin/python3
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
"""
model_state module
"""


Base = declarative_base()


class State(Base):
    """State class inheriting drop Base object"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(1280), nullable=False)


if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    args = sys.argv
    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    p = (pool_pre_ping=True)
    engine = create_engine(conn.format(args[1], args[2], args[3]), p)
    Base.metadata.create_all(engine)
