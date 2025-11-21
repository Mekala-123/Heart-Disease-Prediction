from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime, UTC
now = datetime.now(UTC).isoformat()


class ItemBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class Item(BaseModel):
    id: int
    name: str
    description: str = ""
    created_at: str
    updated_at: str

    model_config = ConfigDict(from_attributes=True)
