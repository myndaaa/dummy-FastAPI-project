"""
Reservation model

Represents a record of a user reserving a specific book in advance.
Holds info on when the reservation was made and its current status.
"""

# SQLAlchemy Imports
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, func
from sqlalchemy.orm import relationship

# Local Imports
from app.database.database import Base


class Reservation(Base):
    __tablename__ = 'reservations'

    # Table columns
    id = Column(Integer, primary_key=True)
    reservation_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    status = Column(String, nullable=False, default="active")  # active, fulfilled, cancelled

    # Foreign keys
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)

    # Relationships
    user = relationship('User', back_populates='reservations')
    book = relationship('Book', back_populates='reservations')

    def __repr__(self):
        return f"<Reservation(id={self.id}, user_id={self.user_id}, book_id={self.book_id}, status='{self.status}')>"
