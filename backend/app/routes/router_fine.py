"""
API routes for Fine
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/fines",
    tags=["fines"]
)


@router.post("/", response_model=schemas.FineOut, status_code=status.HTTP_201_CREATED)
def create_fine(fine: schemas.FineCreate, db: Session = Depends(get_db)):
    """
    Create a new fine.
    """
    return crud.crud_fine.create_fine(db, fine)


@router.get("/{fine_id}", response_model=schemas.FineOut)
def read_fine(fine_id: int, db: Session = Depends(get_db)):
    """
    Get a fine by ID.
    """
    db_fine = crud.crud_fine.get_fine(db, fine_id)
    if not db_fine:
        raise HTTPException(status_code=404, detail="Fine not found")
    return db_fine


@router.get("/", response_model=List[schemas.FineOut])
def read_fines(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of fines.
    """
    return crud.crud_fine.get_fines(db, skip=skip, limit=limit)


@router.patch("/{fine_id}", response_model=schemas.FineOut)
def update_fine(fine_id: int, fine_update: schemas.FineUpdate, db: Session = Depends(get_db)):
    """
    Update a fine by ID.
    """
    db_fine = crud.crud_fine.update_fine(db, fine_id, fine_update)
    if not db_fine:
        raise HTTPException(status_code=404, detail="Fine not found")
    return db_fine


@router.delete("/{fine_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fine(fine_id: int, db: Session = Depends(get_db)):
    """
    Delete a fine by ID.
    """
    success = crud.crud_fine.delete_fine(db, fine_id)
    if not success:
        raise HTTPException(status_code=404, detail="Fine not found")
    return


@router.get("/by_user/{user_id}", response_model=List[schemas.FineOut])
def get_fines_by_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get all fines for a specific user.
    """
    return crud.crud_fine.get_fines_by_user(db, user_id)


@router.get("/unpaid/", response_model=List[schemas.FineOut])
def get_unpaid_fines(user_id: int = None, db: Session = Depends(get_db)):
    """
    Get all unpaid fines, optionally filtered by user.
    """
    return crud.crud_fine.get_unpaid_fines(db, user_id)
