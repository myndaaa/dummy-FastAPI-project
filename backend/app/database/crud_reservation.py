

from sqlalchemy.orm import Session
from typing import List, Optional

from app import models, schemas


def create_reservation(db: Session, reservation: schemas.ReservationCreate) -> models.Reservation:
    """
    Create a new reservation.
    """
    db_reservation = models.Reservation(
        user_id=reservation.user_id,
        book_id=reservation.book_id,
        reservation_date=reservation.reservation_date
    )
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation


def get_reservation(db: Session, reservation_id: int) -> Optional[models.Reservation]:
    """
    Get a reservation by ID.
    """
    return db.query(models.Reservation).filter(models.Reservation.id == reservation_id).first()


def get_reservations(db: Session, skip: int = 0, limit: int = 10) -> List[models.Reservation]:
    """
    Get a list of reservations with pagination.
    """
    return db.query(models.Reservation).offset(skip).limit(limit).all()


def update_reservation(db: Session, reservation_id: int, reservation_update: schemas.ReservationUpdate) -> Optional[models.Reservation]:
    """
    Update a reservation.
    """
    db_reservation = get_reservation(db, reservation_id)
    if not db_reservation:
        return None

    for key, value in reservation_update.model_dump(exclude_unset=True).items():
        setattr(db_reservation, key, value)

    db.commit()
    db.refresh(db_reservation)
    return db_reservation


def delete_reservation(db: Session, reservation_id: int) -> bool:
    """
    Delete a reservation by ID.
    """
    db_reservation = get_reservation(db, reservation_id)
    if not db_reservation:
        return False

    db.delete(db_reservation)
    db.commit()
    return True


def get_reservations_by_user(db: Session, user_id: int) -> List[models.Reservation]:
    """
    Get all reservations for a specific user.
    """
    return db.query(models.Reservation).filter(models.Reservation.user_id == user_id).all()


def get_reservations_by_book(db: Session, book_id: int) -> List[models.Reservation]:
    """
    Get all reservations for a specific book.
    """
    return db.query(models.Reservation).filter(models.Reservation.book_id == book_id).all()
