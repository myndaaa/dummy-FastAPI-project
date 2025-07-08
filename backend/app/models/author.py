"""
Author model

Represents an author who has written one or more books in the library.
"""

# SQLAlchemy Imports
from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.orm import relationship

# Local Imports
from app.database.database import Base


class Author(Base):
    __tablename__ = 'authors'

    # Table columns
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    bio = Column(Text, nullable=True)
    birth_date = Column(Date, nullable=True)

    # Relationships
    books = relationship('Book', back_populates='author', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Author(id={self.id}, name={self.name})>"
