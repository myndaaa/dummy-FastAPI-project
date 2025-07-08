"""
API routes for Author
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/authors",
    tags=["authors"]
)


@router.post("/", response_model=schemas.AuthorOut, status_code=status.HTTP_201_CREATED)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    """
    Create a new author.
    """
    return crud.crud_author.create_author(db, author)


@router.get("/{author_id}", response_model=schemas.AuthorOut)
def read_author(author_id: int, db: Session = Depends(get_db)):
    """
    Get an author by ID.
    """
    db_author = crud.crud_author.get_author(db, author_id)
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@router.get("/", response_model=List[schemas.AuthorOut])
def read_authors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of authors.
    """
    return crud.crud_author.get_authors(db, skip=skip, limit=limit)


@router.patch("/{author_id}", response_model=schemas.AuthorOut)
def update_author(author_id: int, author_update: schemas.AuthorUpdate, db: Session = Depends(get_db)):
    """
    Update an author by ID.
    """
    db_author = crud.crud_author.update_author(db, author_id, author_update)
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    """
    Delete an author by ID.
    """
    success = crud.crud_author.delete_author(db, author_id)
    if not success:
        raise HTTPException(status_code=404, detail="Author not found")
    return


@router.get("/search/", response_model=List[schemas.AuthorOut])
def search_authors(name: str, db: Session = Depends(get_db)):
    """
    Search authors by partial name match.
    """
    return crud.crud_author.search_authors_by_name(db, name)
