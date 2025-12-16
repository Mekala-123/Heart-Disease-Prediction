# src/schemas/item_dto.py
from pydantic import BaseModel
from typing import Optional

class ItemCreateDTO(BaseModel):
    name: str
    description: Optional[str] = None

class ItemUpdateDTO(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class ItemResponseDTO(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
