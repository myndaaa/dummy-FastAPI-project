"""

Pydantic schemas for Author

"""

from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date


class AuthorBase(BaseModel):
    name: str
    bio: Optional[str] = None
    birth_date: Optional[date] = None

    model_config = ConfigDict(from_attributes=True)


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(BaseModel):
    name: Optional[str] = None
    bio: Optional[str] = None
    birth_date: Optional[date] = None

    model_config = ConfigDict(from_attributes=True)


class AuthorInDB(AuthorBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class AuthorOut(AuthorInDB):
    # If you want to return books written by this author
    books: List[str] = []

    model_config = ConfigDict(from_attributes=True)
