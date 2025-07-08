"""

Pydantic schemas for User

"""

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional, List
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    name: str
    phone: Optional[str] = None
    address: Optional[str] = None
    user_access_level: int = Field(1, description="1=USER, 2=LIBRARIAN")
    created_at: Optional[datetime] = None
    disabled_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    password: Optional[str] = None
    user_access_level: Optional[int] = None
    disabled_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class UserInDB(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class UserOut(UserInDB):
    pass
