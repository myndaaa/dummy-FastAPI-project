"""
Fine model

Represents a fine charged to a user for overdue books, lost books, or other penalties. Linked to a specific loan.
"""

# SQLAlchemy Imports
from sqlalchemy import Column, Integer, ForeignKey, Numeric, Boolean, DateTime, func
from sqlalchemy.orm import relationship

# Local Imports
from app.database.database import Base


class Fine(Base):
    __tablename__ = 'fines'

    # Table columns
    id = Column(Integer, primary_key=True)
    amount = Column(Numeric(10, 2), nullable=False)  # e.g. 5.00 dollars
    paid = Column(Boolean, default=False, nullable=False)
    paid_date = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Foreign keys
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    loan_id = Column(Integer, ForeignKey('loans.id'), nullable=False)

    # Relationships
    user = relationship('User', back_populates='fines')
    loan = relationship('Loan', back_populates='fine')

    def __repr__(self):
        return f"<Fine(id={self.id}, amount={self.amount}, paid={self.paid})>"
