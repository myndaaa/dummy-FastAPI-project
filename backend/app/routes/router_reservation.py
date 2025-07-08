

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/reservations",
    tags=["reservations"]
)


@router.post("/", response_model=schemas.ReservationOut, status_code=status.HTTP_201_CREATED)
def create_reservation(reservation: schemas.ReservationCreate, db: Session = Depends(get_db)):
    """
    Create a new reservation.
    """
    return crud.crud_reservation.create_reservation(db, reservation)


@router.get("/{reservation_id}", response_model=schemas.ReservationOut)
def read_reservation(reservation_id: int, db: Session = Depends(get_db)):
    """
    Get a reservation by ID.
    """
    db_reservation = crud.crud_reservation.get_reservation(db, reservation_id)
    if not db_reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return db_reservation


@router.get("/", response_model=List[schemas.ReservationOut])
def read_reservations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of reservations.
    """
    return crud.crud_reservation.get_reservations(db, skip=skip, limit=limit)


@router.patch("/{reservation_id}", response_model=schemas.ReservationOut)
def update_reservation(reservation_id: int, reservation_update: schemas.ReservationUpdate, db: Session = Depends(get_db)):
    """
    Update a reservation by ID.
    """
    db_reservation = crud.crud_reservation.update_reservation(db, reservation_id, reservation_update)
    if not db_reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return db_reservation


@router.delete("/{reservation_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    """
    Delete a reservation by ID.
    """
    success = crud.crud_reservation.delete_reservation(db, reservation_id)
    if not success:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return


@router.get("/by_user/{user_id}", response_model=List[schemas.ReservationOut])
def get_reservations_by_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get all reservations for a specific user.
    """
    return crud.crud_reservation.get_reservations_by_user(db, user_id)


@router.get("/by_book/{book_id}", response_model=List[schemas.ReservationOut])
def get_reservations_by_book(book_id: int, db: Session = Depends(get_db)):
    """
    Get all reservations for a specific book.
    """
    return crud.crud_reservation.get_reservations_by_book(db, book_id)
