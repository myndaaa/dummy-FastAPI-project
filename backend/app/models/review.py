"""
Review model

Represents a users review of a book including a rating and an optional comment
"""

# SQLAlchemy Imports
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

# Local Imports
from app.database.database import Base


class Review(Base):
    __tablename__ = 'reviews'

    # Table columns
    id = Column(Integer, primary_key=True)
    rating = Column(Integer, nullable=False)  # 1–5 stars
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Foreign keys
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)

    # Relationships
    user = relationship('User', back_populates='reviews')
    book = relationship('Book', back_populates='reviews')

    def __repr__(self):
        return f"<Review(id={self.id}, user_id={self.user_id}, book_id={self.book_id}, rating={self.rating})>"
