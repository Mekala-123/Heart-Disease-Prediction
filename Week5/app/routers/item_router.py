from fastapi import APIRouter, HTTPException
from app.schemas.item_schema import ItemCreate, ItemOut
from app.repositories.item_repo_mongo import ItemRepoMongo
from app.core import db

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/", response_model=list[ItemOut])
async def get_items():
    repo = ItemRepoMongo(db.db)
    return await repo.find_many()


@router.post("/", response_model=ItemOut)
async def create_item(item: ItemCreate):
    repo = ItemRepoMongo(db.db)
    return await repo.insert_one(item)


@router.get("/{item_id}", response_model=ItemOut)
async def get_item(item_id: str):
    repo = ItemRepoMongo(db.db)
    item = await repo.find_one(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/{item_id}", response_model=ItemOut)
async def update_item(item_id: str, item: ItemCreate):
    repo = ItemRepoMongo(db.db)
    updated_item = await repo.update_one(item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item


@router.delete("/{item_id}")
async def delete_item(item_id: str):
    repo = ItemRepoMongo(db.db)
    deleted = await repo.delete_one(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}
