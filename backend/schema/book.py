"""

Pydantic schemas for Book

"""

from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List


class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    isbn: str = Field(..., description="Unique ISBN identifier")
    published_year: Optional[int] = None
    total_copies: int = Field(1, description="Total copies available in library")
    available_copies: int = Field(1, description="Number of copies currently available")

    author_id: int
    genre_id: int

    model_config = ConfigDict(from_attributes=True)


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    isbn: Optional[str] = None
    published_year: Optional[int] = None
    total_copies: Optional[int] = None
    available_copies: Optional[int] = None
    author_id: Optional[int] = None
    genre_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class BookInDB(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class BookOut(BookInDB):
    author_name: Optional[str] = None
    genre_name: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
