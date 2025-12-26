from fastapi import APIRouter, HTTPException
from src.services.item_service import (
    fetch_items,
    fetch_item,
    add_item
)

router = APIRouter(prefix="/items", tags=["Items"])

router = APIRouter(prefix="/items", tags=["Items"])

@router.get(
    "/",
    summary="Get all items",
    description="Returns cached items list if available"
)
def get_items():
    return fetch_items()


@router.get(
    "/{item_id}",
    summary="Get item by ID",
    description="Returns cached item if available"
)
def get_item(item_id: int):
    item = fetch_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post(
    "/",
    summary="Create item",
    description="Creates item and invalidates cache"
)
def create_item():
    item = {"id": 3, "name": "Item C"}
    return add_item(item)
