"""

Pydantic schemas for Genre

"""

from pydantic import BaseModel, ConfigDict
from typing import Optional, List


class GenreBase(BaseModel):
    name: str
    description: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class GenreCreate(GenreBase):
    pass


class GenreUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class GenreInDB(GenreBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class GenreOut(GenreInDB):
    books: Optional[List[str]] = []

    model_config = ConfigDict(from_attributes=True)
