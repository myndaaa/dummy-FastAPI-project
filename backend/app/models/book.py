"""
Book model

Represents a book in the library. Each book belongs to one author and one genre, and can be borrowed, reserved, and reviewed by users.
"""

# SQLAlchemy Imports
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

# Local Imports
from app.database.database import Base


class Book(Base):
    __tablename__ = 'books'

    # Table columns
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    isbn = Column(String, unique=True, nullable=False)
    published_year = Column(Integer, nullable=True)
    total_copies = Column(Integer, nullable=False, default=1)
    available_copies = Column(Integer, nullable=False, default=1)

    # Foreign keys
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    genre_id = Column(Integer, ForeignKey('genres.id'), nullable=False)

    # Relationships
    author = relationship('Author', back_populates='books')
    genre = relationship('Genre', back_populates='books')

    loans = relationship('Loan', back_populates='book', cascade="all, delete-orphan")
    reservations = relationship('Reservation', back_populates='book', cascade="all, delete-orphan")
    reviews = relationship('Review', back_populates='book', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', isbn='{self.isbn}')>"
