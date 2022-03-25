import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 


from fastapi import APIRouter, Depends, HTTPException, status
import schemas, database, oauth2
from typing import List
from sqlalchemy.orm import Session
from repository import room

router = APIRouter(
    prefix = "/room",
    tags = ["Rooms"]
)
get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowRoom])
def get_all_rooms(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return room.get_all_rooms(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_room(request: schemas.Room, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return room.create_room(request, db)


@router.get("/get_by_id/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowRoom)
def get_room_by_id(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return room.get_room_by_id(id, db)


@router.get("/get_by_name/{room_name}", status_code=status.HTTP_200_OK, response_model=schemas.ShowRoom)
def get_room_by_name(room_name, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return room.get_room_by_name(room_name, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED) 
def update_single_room(id, request: schemas.Room, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return room.update_single_room(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_single_room(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return room.delete_single_room(id, db)


@router.put("/link/{room_id}/{people_id}", status_code=status.HTTP_202_ACCEPTED)
def link_room_to_people(request: schemas.LinkRoomToPeople, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return room.link_room_to_people(request, db)


@router.put("/unlink/{room_id}/{people_id}", status_code=status.HTTP_202_ACCEPTED)
def unlink_room_to_people(request: schemas.LinkRoomToPeople, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return room.unlink_room_to_people(request, db)


@router.get("/join_room_and_people/", status_code=status.HTTP_200_OK)
def join_room_and_people(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return room.join_room_and_people(db)
