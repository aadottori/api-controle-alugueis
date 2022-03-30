from database import Base
from sqlalchemy import Column, Integer, Boolean, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship


class Room(Base):
    __tablename__ = "rooms"

    room_id = Column(Integer, primary_key=True, index=True)
    room_name = Column(String)
    room_value = Column(Float)
    occupied = Column(Boolean, default=False)
    occupant_id = Column(Integer, ForeignKey("people.people_id"), nullable=True)


class People(Base):
    __tablename__ = "people"

    people_id = Column(Integer, primary_key=True, index=True)
    people_name = Column(String)
    phone = Column(String)
    email = Column(String)
    payday = Column(Integer)
    occupied_room_id = Column(Integer, ForeignKey("rooms.room_id"), nullable=True)


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    username = Column(String)
    password = Column(String)


class Payment(Base):
    __tablename__ = "payments"
    
    payment_id = Column(Integer, index=True)
    room_id = Column(Integer, ForeignKey("rooms.room_id"), primary_key=True)
    people_id = Column(Integer, ForeignKey("people.people_id"), nullable=True)
    month = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    payday = Column(Integer, ForeignKey("people.payday"), nullable=True)
    payment_date = Column(Date)
    room_value = Column(Float, ForeignKey("rooms.room_value"))
    description = Column(String)
    paid = Column(Boolean)


class Light(Base):
    __tablename__ = "light"

    light_id = Column(Integer, index=True)
    room_id = Column(Integer, ForeignKey("rooms.room_id"), primary_key=True)
    month = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    light_value = Column(Float)