"""
User model

Represents a library user who can borrow books, reserve books, write reviews, and pay fines.
"""

# Standard Library
import uuid

# SQLAlchemy Imports
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

# Local Imports
from app.database.database import Base


class User(Base):
    __tablename__ = 'users'

    # Table columns
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  
    phone = Column(String, nullable=True)
    address = Column(String, nullable=True)
    device_uuid = Column(String, default=lambda: str(uuid.uuid4()))
    user_access_level = Column(Integer, nullable=False, default=1)  
    session_token = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now(), nullable=False)
    disabled_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    loans = relationship('Loan', back_populates='user', cascade="all, delete-orphan")
    reservations = relationship('Reservation', back_populates='user', cascade="all, delete-orphan")
    reviews = relationship('Review', back_populates='user', cascade="all, delete-orphan")
    fines = relationship('Fine', back_populates='user', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, name={self.name})>"
