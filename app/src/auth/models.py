import uuid
from datetime import datetime

from fastapi_users import schemas
from pydantic import BaseModel, EmailStr


class Roles(BaseModel):
    id: int
    name: str
    permissions: dict

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int  
    email: EmailStr
    name: str
    password: str
    role_id: int
    registered_at: datetime

    class Config:
        orm_mode = True


class UserRead(schemas.BaseUser[uuid.UUID]):
    id: int
    name: str
    role_id: int


class UserCreate(schemas.BaseUserCreate):
    name: str
    role_id: int


    