from pydantic import BaseModel
from typing import Optional

class ItemCreate(BaseModel):
    name: str
    price: float

class ItemOut(BaseModel):
    id: str
    name: str
    price: float
