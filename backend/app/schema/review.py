"""

Pydantic schemas for Review

"""

from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime


class ReviewBase(BaseModel):
    rating: int = Field(..., ge=1, le=5, description="Rating from 1 to 5 stars")
    comment: Optional[str] = None

    user_id: int
    book_id: int

    model_config = ConfigDict(from_attributes=True)


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    rating: Optional[int] = Field(None, ge=1, le=5)
    comment: Optional[str] = None
    user_id: Optional[int] = None
    book_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class ReviewInDB(ReviewBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ReviewOut(ReviewInDB):
    user_email: Optional[str] = None
    book_title: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
