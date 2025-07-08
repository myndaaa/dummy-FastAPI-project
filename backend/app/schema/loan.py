"""

Pydantic schemas for Loan

"""

from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime


class LoanBase(BaseModel):
    loan_date: Optional[datetime] = None
    due_date: datetime
    return_date: Optional[datetime] = None
    status: str = Field(..., description="Status of the loan: borrowed, returned, overdue")

    user_id: int
    book_id: int

    model_config = ConfigDict(from_attributes=True)


class LoanCreate(LoanBase):
    pass


class LoanUpdate(BaseModel):
    loan_date: Optional[datetime] = None
    due_date: Optional[datetime] = None
    return_date: Optional[datetime] = None
    status: Optional[str] = None
    user_id: Optional[int] = None
    book_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class LoanInDB(LoanBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class LoanOut(LoanInDB):
    user_email: Optional[str] = None
    book_title: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
