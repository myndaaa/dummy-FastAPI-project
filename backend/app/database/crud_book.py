"""
CRUD operations for Book
"""

from sqlalchemy.orm import Session
from typing import List, Optional

from app import models, schemas


def create_book(db: Session, book: schemas.BookCreate) -> models.Book:
    """
    Create a new book.
    """
    db_book = models.Book(
        title=book.title,
        isbn=book.isbn,
        publication_year=book.publication_year,
        copies_available=book.copies_available,
        author_id=book.author_id,
        genre_id=book.genre_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_book(db: Session, book_id: int) -> Optional[models.Book]:
    """
    Get a book by ID.
    """
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_books(db: Session, skip: int = 0, limit: int = 10) -> List[models.Book]:
    """
    Get a list of books with pagination.
    """
    return db.query(models.Book).offset(skip).limit(limit).all()


def update_book(db: Session, book_id: int, book_update: schemas.BookUpdate) -> Optional[models.Book]:
    """
    Update book information.
    """
    db_book = get_book(db, book_id)
    if not db_book:
        return None

    for key, value in book_update.model_dump(exclude_unset=True).items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int) -> bool:
    """
    Delete a book by ID.
    """
    db_book = get_book(db, book_id)
    if not db_book:
        return False

    db.delete(db_book)
    db.commit()
    return True


def search_books_by_title(db: Session, title_substring: str) -> List[models.Book]:
    """
    Search books by title (case-insensitive).
    """
    return db.query(models.Book).filter(models.Book.title.ilike(f"%{title_substring}%")).all()


def get_books_by_author(db: Session, author_id: int) -> List[models.Book]:
    """
    Get all books by a specific author.
    """
    return db.query(models.Book).filter(models.Book.author_id == author_id).all()


def get_books_by_genre(db: Session, genre_id: int) -> List[models.Book]:
    """
    Get all books of a specific genre.
    """
    return db.query(models.Book).filter(models.Book.genre_id == genre_id).all()
