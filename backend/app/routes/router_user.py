"""
API routes for User.

Connects HTTP endpoints to CRUD logic.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import crud, models, schemas
from app.database import get_db  

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post("/", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    db_user = crud.crud_user.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.crud_user.create_user(db, user)


@router.get("/{user_id}", response_model=schemas.UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get a user by ID.
    """
    db_user = crud.crud_user.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/", response_model=List[schemas.UserOut])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of users.
    """
    return crud.crud_user.get_users(db, skip=skip, limit=limit)


@router.patch("/{user_id}", response_model=schemas.UserOut)
def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    """
    Update a user by ID.
    """
    db_user = crud.crud_user.update_user(db, user_id, user_update)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Delete a user by ID.
    """
    success = crud.crud_user.delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return


@router.get("/by_access_level/{level}", response_model=List[schemas.UserOut])
def get_users_by_access_level(level: int, db: Session = Depends(get_db)):
    """
    Get all users with a specific access level.
    """
    return crud.crud_user.get_users_by_access_level(db, level)


@router.get("/search/", response_model=List[schemas.UserOut])
def search_users(name: str, db: Session = Depends(get_db)):
    """
    Search users by partial name match.
    """
    return crud.crud_user.search_users_by_name(db, name)
