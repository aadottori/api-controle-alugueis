import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status


def get_all_peoples(db: Session):
    peoples = db.query(models.People).all()
    return peoples


def create_people(request: schemas.People, db: Session):
    new_people = models.People(
                        people_name=request.people_name, 
                        phone=request.phone, 
                        email=request.email,
                        payday=request.payday,
                        )
    db.add(new_people)
    db.commit()
    db.refresh(new_people)
    return new_people


def get_single_people(id, db: Session):
    people = db.query(models.People).filter(models.People.people_id == id).first()
    if not people:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"People with id {id} not available.")
    return people


def delete_single_people(id, db: Session):
    people = db.query(models.People).filter(models.People.people_id == id)
    if not people.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"People with id {id} not available.")
    people.delete(synchronize_session=False)
    db.commit()
    return "Done"


def update_single_people(id, request: schemas.People, db: Session):
    people = db.query(models.People).filter(models.People.people_id == id)
    if not people.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"People with id {id} not available.")
    people.update(request.dict()) 
    db.commit() 
    return "Update"
