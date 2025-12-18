from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    roles: Optional[List[str]] = ["user"]

class UserOut(BaseModel):
    email: EmailStr
    roles: List[str]

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"