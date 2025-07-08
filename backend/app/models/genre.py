"""
Genre model

Represents a book category or genre, such as Fiction, Non-fiction, Mystery, etc.
"""

# SQLAlchemy Imports
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

# Local Imports
from app.database.database import Base


class Genre(Base):
    __tablename__ = 'genres'

    # Table columns
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=True)

    # Relationships
    books = relationship('Book', back_populates='genre', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Genre(id={self.id}, name='{self.name}')>"
