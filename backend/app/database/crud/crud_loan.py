"""
CRUD operations for Loan
"""

from sqlalchemy.orm import Session
from typing import List, Optional

from app import models, schemas


def create_loan(db: Session, loan: schemas.LoanCreate) -> models.Loan:
    """
    Create a new loan.
    """
    db_loan = models.Loan(
        user_id=loan.user_id,
        book_id=loan.book_id,
        loan_date=loan.loan_date,
        return_date=loan.return_date
    )
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan


def get_loan(db: Session, loan_id: int) -> Optional[models.Loan]:
    """
    Get a loan by ID.
    """
    return db.query(models.Loan).filter(models.Loan.id == loan_id).first()


def get_loans(db: Session, skip: int = 0, limit: int = 10) -> List[models.Loan]:
    """
    Get a list of loans with pagination.
    """
    return db.query(models.Loan).offset(skip).limit(limit).all()


def update_loan(db: Session, loan_id: int, loan_update: schemas.LoanUpdate) -> Optional[models.Loan]:
    """
    Update a loan.
    """
    db_loan = get_loan(db, loan_id)
    if not db_loan:
        return None

    for key, value in loan_update.model_dump(exclude_unset=True).items():
        setattr(db_loan, key, value)

    db.commit()
    db.refresh(db_loan)
    return db_loan


def delete_loan(db: Session, loan_id: int) -> bool:
    """
    Delete a loan by ID.
    """
    db_loan = get_loan(db, loan_id)
    if not db_loan:
        return False

    db.delete(db_loan)
    db.commit()
    return True


def get_loans_by_user(db: Session, user_id: int) -> List[models.Loan]:
    """
    Get all loans for a specific user.
    """
    return db.query(models.Loan).filter(models.Loan.user_id == user_id).all()


def get_loans_by_book(db: Session, book_id: int) -> List[models.Loan]:
    """
    Get all loans for a specific book.
    """
    return db.query(models.Loan).filter(models.Loan.book_id == book_id).all()


def get_active_loans(db: Session, user_id: Optional[int] = None) -> List[models.Loan]:
    """
    Get all active (not yet returned) loans.
    Optionally filter by user.
    """
    query = db.query(models.Loan).filter(models.Loan.return_date == None)
    if user_id:
        query = query.filter(models.Loan.user_id == user_id)
    return query.all()
