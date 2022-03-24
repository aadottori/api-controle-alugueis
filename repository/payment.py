import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status



def get_all_payments(db: Session):
    payments = db.query(models.Payment).all()
    return payments


def create_payment(request: schemas.Payment, db: Session):
    new_payment = models.Payment(
                            id = request.id,
                            room_id=request.room_id,
                            people_id=request.people_id,
                            month=request.month,
                            year=request.year,
                            payday=request.payday,
                            payment_date=request.payment_date,
                            value=request.value,
                            paid=request.paid,
                        )
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment


def get_payment_by_id(id, db: Session):
    payment = db.query(models.Payment).filter(models.Payment.id == id).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Payment with id {id} not available.")
    return payment


def get_payment_by_month_year(month, year, db: Session):
    payment = db.query(models.Payment).filter(models.Payment.month == month).filter(models.Payment.year == year).all()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Payments from {month}/{year} not available.")
    return payment


def get_payment_by_roomId_month_year(room_id, month, year, db: Session):
    payment = db.query(models.Payment).filter(models.Payment.room_id == room_id).filter(models.Payment.month == month).filter(models.Payment.year == year).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Payment with room ID {room_id}, from {month}/{year} not available.")
    return payment


def get_months_with_registered_payments(db: Session):
    months = db.query(models.Payment.month, models.Payment.year).group_by(models.Payment.month, models.Payment.year).all()
    if not months:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No months registeresd.")
    return months


def delete_single_payment(id, db: Session):
    payment = db.query(models.Payment).filter(models.Payment.id == id)
    if not payment.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Payment with id {id} not available.")
    payment.delete(synchronize_session=False)
    db.commit()
    return "Done"


def update_single_payment(id, request: schemas.Payment, db: Session):
    payment = db.query(models.Payment).filter(models.Payment.id == id)
    if not payment.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Payment with id {id} not available.")
    payment.update(request.dict()) 
    db.commit() 
    return "Updated"
