"""
CRUD operations for User
"""

from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from app import models, schemas
from typing import List, Optional
from app.database.database import SessionLocal, Base

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    """
    Create a new user in the database.
    """
    db_user = models.User(
        email=user.email,
        name=user.name,
        phone=user.phone,
        address=user.address,
        password=user.password,  
        user_access_level=user.user_access_level
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int) -> Optional[models.User]:
    """
    Get a user by ID.
    """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    """
    Get a user by their email.
    """
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 10) -> List[models.User]:
    """
    Get a list of users with pagination.
    """
    return db.query(models.User).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate) -> Optional[models.User]:
    """
    Update a user's info.
    """
    db_user = get_user(db, user_id)
    if not db_user:
        return None

    for key, value in user_update.model_dump(exclude_unset=True).items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int) -> bool:
    """
    Delete a user by ID.
    """
    db_user = get_user(db, user_id)
    if not db_user:
        return False

    db.delete(db_user)
    db.commit()
    return True


def get_users_by_access_level(db: Session, level: int) -> List[models.User]:
    """
    Get all users with a specific access level.
    """
    return db.query(models.User).filter(models.User.user_access_level == level).all()


def search_users_by_name(db: Session, name_substring: str) -> List[models.User]:
    """
    Get all users whose names contain the given substring (case-insensitive).
    """
    return db.query(models.User).filter(models.User.name.ilike(f"%{name_substring}%")).all()
