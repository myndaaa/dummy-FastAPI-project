"""

Pydantic schemas for Reservation

"""

from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime


class ReservationBase(BaseModel):
    reservation_date: Optional[datetime] = None
    status: str = Field(..., description="Status: active, fulfilled, cancelled")

    user_id: int
    book_id: int

    model_config = ConfigDict(from_attributes=True)


class ReservationCreate(ReservationBase):
    pass


class ReservationUpdate(BaseModel):
    reservation_date: Optional[datetime] = None
    status: Optional[str] = None
    user_id: Optional[int] = None
    book_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class ReservationInDB(ReservationBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ReservationOut(ReservationInDB):
    user_email: Optional[str] = None
    book_title: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
