from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId


class Item(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    name: str
    price: float

    class Config:
        populate_by_name = True

    @staticmethod
    def mongo_to_dict(doc):
     return {
        "id": str(doc.get("_id", "")),
        "name": doc.get("name", ""),
        "price": doc.get("price", 0)
    }

