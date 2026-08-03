from datetime import date, datetime

from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    birth_date: date | None = None


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    last_name: str
    email: EmailStr
    birth_date: date | None
    language: str
    timezone: str
    is_active: bool
    is_verified: bool
    created_at: datetime
