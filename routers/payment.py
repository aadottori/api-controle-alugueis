import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 


from fastapi import APIRouter, Depends, HTTPException, status
import schemas, database, oauth2
from typing import List
from sqlalchemy.orm import Session
from repository import payment

router = APIRouter(
    prefix = "/payment",
    tags = ["Payments"]
)
get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowPayment])
def get_all_payments(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return payment.get_all_payments(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_payment(request: schemas.Payment, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return payment.create_payment(request, db)


@router.get("/get_by_id/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowPayment)
def get_payment_by_id(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return payment.get_payment_by_id(id, db)


@router.get("/get_by_month_year/{month}/{year}", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowPayment])
def get_payment_by_month_year(month, year, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return payment.get_payment_by_month_year(month, year, db)


@router.get("/get_by_roomId_month_year/{room_id}/{month}/{year}", status_code=status.HTTP_200_OK, response_model=schemas.ShowPayment)
def get_payment_by_roomId_month_year(room_id, month, year, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return payment.get_payment_by_roomId_month_year(room_id, month, year, db)

@router.get("/get_registered_months/", status_code=status.HTTP_200_OK)
def get_months_with_registered_payments(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return payment.get_months_with_registered_payments(db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED) 
def update_single_payment(id, request: schemas.Payment, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return payment.update_single_payment(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_single_payment(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return payment.delete_single_payment(id, db)


@router.get("/join_payment_and_room_and_people/", status_code=status.HTTP_200_OK)
def join_payment_and_room_and_people(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return payment.join_payment_and_room_and_people(db)



