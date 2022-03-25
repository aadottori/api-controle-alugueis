import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from sqlalchemy.orm import Session, join
import models, schemas
from fastapi import HTTPException, status



def get_all_lights(db: Session):
    lights = db.query(models.Light).all()
    return lights


def create_light(request: schemas.Light, db: Session):
    new_light = models.Light(
                        id=request.id,
                        room_id=request.room_id,
                        month=request.month,
                        year=request.year,
                        value=request.value, 
                        )
    db.add(new_light)
    db.commit()
    db.refresh(new_light)
    return new_light


def get_light_by_id(id, db: Session):
    light = db.query(models.Light).filter(models.Light.id == id).first()
    if not light:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Light with id {id} not available.")
    return light

def delete_single_light(id, db: Session):
    light = db.query(models.Light).filter(models.Light.id == id)
    if not light.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Light with id {id} not available.")
    light.delete(synchronize_session=False)
    db.commit()
    return "Done"


def update_single_light(id, request: schemas.Light, db: Session):
    light = db.query(models.Light).filter(models.Light.id == id)
    if not light.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Light with id {id} not available.")
    light.update(request.dict()) 
    db.commit() 
    return "Update"
    
def get_light_by_month_year(month, year, db: Session):
    light = db.query(models.Light).filter(models.Light.month == month).filter(models.Light.year == year).all()
    if not light:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Lights from {month}/{year} not available.")
    return light


def get_light_by_roomId_month_year(room_id, month, year, db: Session):
    light = db.query(models.Light).filter(models.Light.room_id == room_id).filter(models.Light.month == month).filter(models.Light.year == year).first()
    if not light:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Light with light ID {room_id}, from {month}/{year} not available.")
    return light

def get_months_with_registered_lights(db: Session):
    months = db.query(models.Light.month, models.Light.year).group_by(models.Light.month, models.Light.year).all()
    if not months:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No months registeresd.")
    return months

def join_light_and_room(db:Session):
    room = models.Room
    light = models.Light
    inner_join = db.query(light, room).join(room, room.id == light.room_id).all()
    light_and_room = []
    for result in inner_join:
        dict_to_append = {}
        for model in result:
            model = model.__dict__
            for key in model:
                if key not in dict_to_append.keys():
                    dict_to_append[key] = model[key]
        light_and_room.append(dict_to_append)

    return light_and_room

