"""
API routes for Book
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/books",
    tags=["books"]
)


@router.post("/", response_model=schemas.BookOut, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    Create a new book.
    """
    return crud.crud_book.create_book(db, book)


@router.get("/{book_id}", response_model=schemas.BookOut)
def read_book(book_id: int, db: Session = Depends(get_db)):
    """
    Get a book by ID.
    """
    db_book = crud.crud_book.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.get("/", response_model=List[schemas.BookOut])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of books.
    """
    return crud.crud_book.get_books(db, skip=skip, limit=limit)


@router.patch("/{book_id}", response_model=schemas.BookOut)
def update_book(book_id: int, book_update: schemas.BookUpdate, db: Session = Depends(get_db)):
    """
    Update a book by ID.
    """
    db_book = crud.crud_book.update_book(db, book_id, book_update)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Delete a book by ID.
    """
    success = crud.crud_book.delete_book(db, book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return


@router.get("/search/", response_model=List[schemas.BookOut])
def search_books(title: str, db: Session = Depends(get_db)):
    """
    Search books by partial title match.
    """
    return crud.crud_book.search_books_by_title(db, title)


@router.get("/by_author/{author_id}", response_model=List[schemas.BookOut])
def get_books_by_author(author_id: int, db: Session = Depends(get_db)):
    """
    Get all books by a specific author.
    """
    return crud.crud_book.get_books_by_author(db, author_id)


@router.get("/by_genre/{genre_id}", response_model=List[schemas.BookOut])
def get_books_by_genre(genre_id: int, db: Session = Depends(get_db)):
    """
    Get all books of a specific genre.
    """
    return crud.crud_book.get_books_by_genre(db, genre_id)
