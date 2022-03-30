from pydantic import BaseModel
from typing import List, Optional
import datetime


"""ROOM SCHEMAS"""
class RoomBase(BaseModel):
    room_id: Optional[int]
    room_name: str
    room_value: float
    occupied: bool
    occupant_id: Optional[int]

class Room(RoomBase):
    class Config():
        orm_mode = True

"""PEOPLE SCHEMAS"""
class PeopleBase(BaseModel):
    people_id: Optional[int]
    people_name: str
    phone: str
    email: str
    payday: int
    occupied_room_id: Optional[int]

class People(PeopleBase):
    class Config():
        orm_mode = True

"""USER SCHEMAS"""
class UserBase(BaseModel):
    user_id: Optional[int]
    name: str
    email: str
    username: str
    password: str

class User(UserBase):
    class Config():
        orm_mode = True

"""PAYMENT SCHEMAS"""
class PaymentBase(BaseModel):
    payment_id: Optional[int]
    room_id: int
    people_id: Optional[int]
    month: int
    year: int
    payday: Optional[int]
    payment_date: datetime.date
    room_value: float
    description: str
    paid: bool

class Payment(PaymentBase):
    class Config():
        orm_mode = True

"""LOGIN SCHEMAS"""
class Login(BaseModel):
    username: str
    password: str


class LinkRoomToPeople(BaseModel):
    room_id: int
    people_id: int

"""LIGHT SCHEMAS"""
class LightBase(BaseModel):
    light_id: Optional[int]
    room_id: int
    month: int
    year: int
    light_value: float

class Light(LightBase):
    class Config():
        orm_mode = True

"""TOKEN SCHEMAS"""
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


"""SHOW SCHEMAS"""
class ShowUser(User):
    name: str
    email: str
    username: str
    class Config():
        orm_mode = True


class ShowPeople(People):
    people_name: str
    phone: str
    email: str
    payday: int
    occupied_room_id: Optional[int]
    class Config():
        orm_mode = True


class ShowRoom(Room):
    room_name: str
    room_value: float
    occupied: bool
    occupant_id: Optional[int] = None
    class Config():
        orm_mode = True


class ShowPayment(Payment):
    payment_id: Optional[int]
    room_id: int
    people_id: Optional[int]
    month: int
    year: int
    payday: Optional[int]
    payment_date: datetime.date
    room_value: float
    paid: bool
    class Config():
        orm_mode = True

class ShowLight(Light):
    light_id: Optional[int]
    room_id: int
    month: int
    year: int
    light_value: float
    class Config():
        orm_mode = True