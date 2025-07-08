
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/loans",
    tags=["loans"]
)


@router.post("/", response_model=schemas.LoanOut, status_code=status.HTTP_201_CREATED)
def create_loan(loan: schemas.LoanCreate, db: Session = Depends(get_db)):
    """
    Create a new loan.
    """
    return crud.crud_loan.create_loan(db, loan)


@router.get("/{loan_id}", response_model=schemas.LoanOut)
def read_loan(loan_id: int, db: Session = Depends(get_db)):
    """
    Get a loan by ID.
    """
    db_loan = crud.crud_loan.get_loan(db, loan_id)
    if not db_loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan


@router.get("/", response_model=List[schemas.LoanOut])
def read_loans(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of loans.
    """
    return crud.crud_loan.get_loans(db, skip=skip, limit=limit)


@router.patch("/{loan_id}", response_model=schemas.LoanOut)
def update_loan(loan_id: int, loan_update: schemas.LoanUpdate, db: Session = Depends(get_db)):
    """
    Update a loan by ID.
    """
    db_loan = crud.crud_loan.update_loan(db, loan_id, loan_update)
    if not db_loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan


@router.delete("/{loan_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_loan(loan_id: int, db: Session = Depends(get_db)):
    """
    Delete a loan by ID.
    """
    success = crud.crud_loan.delete_loan(db, loan_id)
    if not success:
        raise HTTPException(status_code=404, detail="Loan not found")
    return


@router.get("/by_user/{user_id}", response_model=List[schemas.LoanOut])
def get_loans_by_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get all loans for a specific user.
    """
    return crud.crud_loan.get_loans_by_user(db, user_id)


@router.get("/by_book/{book_id}", response_model=List[schemas.LoanOut])
def get_loans_by_book(book_id: int, db: Session = Depends(get_db)):
    """
    Get all loans for a specific book.
    """
    return crud.crud_loan.get_loans_by_book(db, book_id)


@router.get("/active/", response_model=List[schemas.LoanOut])
def get_active_loans(user_id: int = None, db: Session = Depends(get_db)):
    """
    Get all active loans (not yet returned).
    Optionally filter by user.
    """
    return crud.crud_loan.get_active_loans(db, user_id)
