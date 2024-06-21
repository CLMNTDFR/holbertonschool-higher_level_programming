#!/usr/bin/python3
"""Nameless module to declare tables for db hbtn_0e_6_usa
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class to declare the states database table"""

    __tablename__ = "states"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
