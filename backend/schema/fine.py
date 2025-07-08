"""

Pydantic schemas for Fine

"""

from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal


class FineBase(BaseModel):
    amount: Decimal = Field(..., description="Amount charged for the fine")
    paid: bool = False
    paid_date: Optional[datetime] = None

    user_id: int
    loan_id: int

    model_config = ConfigDict(from_attributes=True)


class FineCreate(FineBase):
    pass


class FineUpdate(BaseModel):
    amount: Optional[Decimal] = None
    paid: Optional[bool] = None
    paid_date: Optional[datetime] = None
    user_id: Optional[int] = None
    loan_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class FineInDB(FineBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class FineOut(FineInDB):
    user_email: Optional[str] = None
    loan_status: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
