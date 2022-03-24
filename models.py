from database import Base
from sqlalchemy import Column, Integer, Boolean, String, Float, Date, ForeignKey
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


class Payment(Base):
    __tablename__ = "payments"
    
    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"), primary_key=True)
    people_id = Column(Integer, ForeignKey("people.id"), nullable=True)
    month = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    payday = Column(Integer, ForeignKey("people.payday"), nullable=True)
    payment_date = Column(Date)
    value = Column(Float, ForeignKey("rooms.value"))
    paid = Column(Boolean)
