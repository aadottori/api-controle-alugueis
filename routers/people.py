import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 


from fastapi import APIRouter, Depends, HTTPException, status
import schemas, database, oauth2
from typing import List
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from repository import people


router = APIRouter(
    prefix = "/people",
    tags = ["Peoples"],
)
get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowPeople])
def get_all_peoples(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return people.get_all_peoples(db)


@router.post("/", response_model=schemas.ShowPeople)
def create_people(request: schemas.People, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return people.create_people(request, db)


@router.get("/{id}", response_model = schemas.ShowPeople)
def get_single_people(id:int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return people.get_single_people(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED) 
def update_single_people(id, request: schemas.People, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return people.update_single_people(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_single_people(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return people.delete_single_people(id, db)


