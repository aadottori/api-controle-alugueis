import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 


from fastapi import APIRouter, Depends, HTTPException, status
import schemas, database, oauth2
from typing import List
from sqlalchemy.orm import Session
from repository import light

router = APIRouter(
    prefix = "/light",
    tags = ["Lights"]
)
get_db = database.get_db

@router.get("/", response_model=List[schemas.ShowLight])
def get_all_lights(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return light.get_all_lights(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_light(request: schemas.Light, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return light.create_light(request, db)


@router.get("/get_by_id/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowLight)
def get_light_by_id(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return light.get_light_by_id(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED) 
def update_single_light(id, request: schemas.Light, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return light.update_single_light(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_single_light(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return light.delete_single_light(id, db)

@router.get("/get_by_month_year/{month}/{year}", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowLight])
def get_light_by_month_year(month, year, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return light.get_light_by_month_year(month, year, db)


@router.get("/get_by_roomId_month_year/{room_id}/{month}/{year}", status_code=status.HTTP_200_OK, response_model=schemas.ShowLight)
def get_light_by_roomId_month_year(room_id, month, year, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return light.get_light_by_roomId_month_year(room_id, month, year, db)

@router.get("/get_registered_months/", status_code=status.HTTP_200_OK)
def get_months_with_registered_lights(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return light.get_months_with_registered_lights(db)


