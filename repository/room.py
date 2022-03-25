import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from sqlalchemy.orm import Session, join
import models, schemas
from fastapi import HTTPException, status



def get_all_rooms(db: Session):
    rooms = db.query(models.Room).all()
    return rooms


def create_room(request: schemas.Room, db: Session):
    new_room = models.Room(
                        room_name=request.room_name, 
                        value=request.value, 
                        )
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room


def get_room_by_id(id, db: Session):
    room = db.query(models.Room).filter(models.Room.id == id).first()
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Room with id {id} not available.")
    return room


def get_room_by_name(room_name, db: Session):
    room = db.query(models.Room).filter(models.Room.room_name == room_name).first()
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Room with name {room_name} not available.")
    return room


def delete_single_room(id, db: Session):
    room = db.query(models.Room).filter(models.Room.id == id)
    if not room.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Room with id {id} not available.")
    room.delete(synchronize_session=False)
    db.commit()
    return "Done"


def update_single_room(id, request: schemas.Room, db: Session):
    room = db.query(models.Room).filter(models.Room.id == id)
    if not room.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Room with id {id} not available.")
    room.update(request.dict()) 
    db.commit() 
    return "Update"


def link_room_to_people(request: schemas.LinkRoomToPeople, db: Session):
    room = db.query(models.Room).filter(models.Room.id == request.room_id)
    people = db.query(models.People).filter(models.People.id == request.people_id)
    if not room.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Room with id {id} not available.")
    if not people.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"People with id {id} not available.")
    new_room = {
        "id": request.room_id,
        "room_name": room.first().room_name,
        "value": room.first().value,
        "occupied": True,
        "occupant_id": request.people_id
    }
    room.update(new_room) 
    db.commit()
    return "linked"


def unlink_room_to_people(request: schemas.LinkRoomToPeople, db: Session):
    room = db.query(models.Room).filter(models.Room.id == request.room_id)
    if not room.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Room with id {id} not available.")
    new_room = {
        "id": request.room_id,
        "room_name": room.first().room_name,
        "value": room.first().value,
        "occupied": False,
        "occupant_id": None
    }
    room.update(new_room) 
    db.commit()
    return "unlinked"


def join_room_and_people(db:Session):
    # quartos ocupados
    room = models.Room
    people = models.People
    inner_join = db.query(room, people).join(people, room.occupant_id == people.id).all()
    occupied_rooms = []
    for result in inner_join:
        dict_to_append = {}
        for model in result:
            model = model.__dict__
            for key in model:
                if key not in dict_to_append.keys():
                    dict_to_append[key] = model[key]
        occupied_rooms.append(dict_to_append)
    
    #quartos não ocupados
    disocuppied_rooms = db.query(models.Room).filter(models.Room.occupied == False).all()


    return occupied_rooms + disocuppied_rooms

