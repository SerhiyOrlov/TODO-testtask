from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime

from sqlalchemy.orm import DeclarativeBase

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


    