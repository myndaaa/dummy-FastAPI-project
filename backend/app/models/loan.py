"""
Loan model

Represents a record of a user borrowing a specific book. Tracks when the book was borrowed, when it’s due, when it’s returned, and links to any fines if applicable.
"""

# SQLAlchemy Imports
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, func
from sqlalchemy.orm import relationship

# Local Imports
from app.database.database import Base


class Loan(Base):
    __tablename__ = 'loans'

    # Table columns
    id = Column(Integer, primary_key=True)
    loan_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    due_date = Column(DateTime(timezone=True), nullable=False)
    return_date = Column(DateTime(timezone=True), nullable=True)
    status = Column(String, nullable=False, default="borrowed")  # borrowed, returned, overdue

    # Foreign keys
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)

    # Relationships
    user = relationship('User', back_populates='loans')
    book = relationship('Book', back_populates='loans')
    fine = relationship('Fine', back_populates='loan', uselist=False, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Loan(id={self.id}, user_id={self.user_id}, book_id={self.book_id}, status='{self.status}')>"
