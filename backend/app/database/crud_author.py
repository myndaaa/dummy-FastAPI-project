"""
CRUD operations for Author
"""

from sqlalchemy.orm import Session
from typing import List, Optional

from app import models, schemas


def create_author(db: Session, author: schemas.AuthorCreate) -> models.Author:
    """
    Create a new author.
    """
    db_author = models.Author(
        name=author.name,
        bio=author.bio
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_author(db: Session, author_id: int) -> Optional[models.Author]:
    """
    Get an author by ID.
    """
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def get_authors(db: Session, skip: int = 0, limit: int = 10) -> List[models.Author]:
    """
    Get a list of authors with pagination.
    """
    return db.query(models.Author).offset(skip).limit(limit).all()


def update_author(db: Session, author_id: int, author_update: schemas.AuthorUpdate) -> Optional[models.Author]:
    """
    Update an author's information.
    """
    db_author = get_author(db, author_id)
    if not db_author:
        return None

    for key, value in author_update.model_dump(exclude_unset=True).items():
        setattr(db_author, key, value)

    db.commit()
    db.refresh(db_author)
    return db_author


def delete_author(db: Session, author_id: int) -> bool:
    """
    Delete an author by ID.
    """
    db_author = get_author(db, author_id)
    if not db_author:
        return False

    db.delete(db_author)
    db.commit()
    return True


def search_authors_by_name(db: Session, name_substring: str) -> List[models.Author]:
    """
    Search authors by name (case-insensitive).
    """
    return db.query(models.Author).filter(models.Author.name.ilike(f"%{name_substring}%")).all()
