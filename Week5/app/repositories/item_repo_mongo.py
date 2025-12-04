from bson import ObjectId
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException
from app.models.item import Item
from app.schemas.item_schema import ItemCreate

class ItemRepoMongo:
    def __init__(self, db_instance):
        self.db = db_instance

    @property
    def collection(self):
        if self.db is None:
            raise Exception("MongoDB not connected. Call connect_to_mongo first.")
        return self.db.get_collection("items")

    async def insert_one(self, item: ItemCreate):
        doc = item.model_dump()  # Pydantic V2 uses model_dump instead of dict
        try:
            result = await self.collection.insert_one(doc)
        except DuplicateKeyError:
            raise HTTPException(status_code=400, detail=f"Item with name '{item.name}' already exists")

        new_doc = await self.collection.find_one({"_id": result.inserted_id})
        return Item.mongo_to_dict(new_doc)

    async def find_one(self, item_id: str):
        try:
            oid = ObjectId(item_id)
        except Exception:
            return None
        doc = await self.collection.find_one({"_id": oid})
        return Item.mongo_to_dict(doc) if doc else None

    async def find_many(self):
        items = []
        async for doc in self.collection.find():
            items.append(Item.mongo_to_dict(doc))
        return items

    async def update_one(self, item_id: str, item: ItemCreate):
        try:
            oid = ObjectId(item_id)
        except Exception:
            return None
        await self.collection.update_one({"_id": oid}, {"$set": item.model_dump()})
        updated = await self.collection.find_one({"_id": oid})
        return Item.mongo_to_dict(updated) if updated else None

    async def delete_one(self, item_id: str):
        try:
            oid = ObjectId(item_id)
        except Exception:
            return False
        result = await self.collection.delete_one({"_id": oid})
        return result.deleted_count > 0
