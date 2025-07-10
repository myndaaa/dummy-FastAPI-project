"""
CRUD operations for Fine
"""

from sqlalchemy.orm import Session
from typing import List, Optional

from app import models, schemas


def create_fine(db: Session, fine: schemas.FineCreate) -> models.Fine:
    """
    Create a new fine.
    """
    db_fine = models.Fine(
        user_id=fine.user_id,
        amount=fine.amount,
        paid=fine.paid,
        issued_at=fine.issued_at
    )
    db.add(db_fine)
    db.commit()
    db.refresh(db_fine)
    return db_fine


def get_fine(db: Session, fine_id: int) -> Optional[models.Fine]:
    """
    Get a fine by ID.
    """
    return db.query(models.Fine).filter(models.Fine.id == fine_id).first()


def get_fines(db: Session, skip: int = 0, limit: int = 10) -> List[models.Fine]:
    """
    Get a list of fines with pagination.
    """
    return db.query(models.Fine).offset(skip).limit(limit).all()


def update_fine(db: Session, fine_id: int, fine_update: schemas.FineUpdate) -> Optional[models.Fine]:
    """
    Update a fine.
    """
    db_fine = get_fine(db, fine_id)
    if not db_fine:
        return None

    for key, value in fine_update.model_dump(exclude_unset=True).items():
        setattr(db_fine, key, value)

    db.commit()
    db.refresh(db_fine)
    return db_fine


def delete_fine(db: Session, fine_id: int) -> bool:
    """
    Delete a fine by ID.
    """
    db_fine = get_fine(db, fine_id)
    if not db_fine:
        return False

    db.delete(db_fine)
    db.commit()
    return True


def get_fines_by_user(db: Session, user_id: int) -> List[models.Fine]:
    """
    Get all fines for a specific user.
    """
    return db.query(models.Fine).filter(models.Fine.user_id == user_id).all()


def get_unpaid_fines(db: Session, user_id: Optional[int] = None) -> List[models.Fine]:
    """
    Get all unpaid fines, optionally filtered by user.
    """
    query = db.query(models.Fine).filter(models.Fine.paid == False)
    if user_id:
        query = query.filter(models.Fine.user_id == user_id)
    return query.all()
