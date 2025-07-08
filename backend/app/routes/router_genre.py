"""
API routes for Genre
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/genres",
    tags=["genres"]
)


@router.post("/", response_model=schemas.GenreOut, status_code=status.HTTP_201_CREATED)
def create_genre(genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    """
    Create a new genre.
    """
    return crud.crud_genre.create_genre(db, genre)


@router.get("/{genre_id}", response_model=schemas.GenreOut)
def read_genre(genre_id: int, db: Session = Depends(get_db)):
    """
    Get a genre by ID.
    """
    db_genre = crud.crud_genre.get_genre(db, genre_id)
    if not db_genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre


@router.get("/", response_model=List[schemas.GenreOut])
def read_genres(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of genres.
    """
    return crud.crud_genre.get_genres(db, skip=skip, limit=limit)


@router.patch("/{genre_id}", response_model=schemas.GenreOut)
def update_genre(genre_id: int, genre_update: schemas.GenreUpdate, db: Session = Depends(get_db)):
    """
    Update a genre by ID.
    """
    db_genre = crud.crud_genre.update_genre(db, genre_id, genre_update)
    if not db_genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre


@router.delete("/{genre_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    """
    Delete a genre by ID.
    """
    success = crud.crud_genre.delete_genre(db, genre_id)
    if not success:
        raise HTTPException(status_code=404, detail="Genre not found")
    return


@router.get("/search/", response_model=List[schemas.GenreOut])
def search_genres(name: str, db: Session = Depends(get_db)):
    """
    Search genres by partial name match.
    """
    return crud.crud_genre.search_genres_by_name(db, name)
