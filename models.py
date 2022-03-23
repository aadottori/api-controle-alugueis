from database import Base
from sqlalchemy import Column, Integer, Boolean, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    room_name = Column(String)
    value = Column(Float)
    occupied = Column(Boolean, default=False)
    occupant_id = Column(Integer, ForeignKey("people.id"), nullable=True)


class People(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    payday = Column(Integer)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    username = Column(String)
    password = Column(String)