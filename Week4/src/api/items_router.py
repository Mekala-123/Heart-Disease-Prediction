from fastapi import APIRouter, Depends, HTTPException, Query, Path
from typing import Optional
from src.schemas.item import ItemCreate, ItemUpdate, Item
from src.services.item_service import ItemService
from src.core.errors import NotFoundError   # Correct import

router = APIRouter()

def get_service():
    return ItemService()


@router.post("/", response_model=Item, summary="Create an item")
def create_item(payload: ItemCreate, svc: ItemService = Depends(get_service)):
    try:
        return svc.create_item(payload.dict())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", summary="List items with optional search and pagination")
def list_items(
    q: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    svc: ItemService = Depends(get_service),
):
    return svc.list_items(q=q, page=page, size=size)


@router.get("/{item_id}", response_model=Item, summary="Get one item by id")
def get_item(item_id: int = Path(..., ge=1), svc: ItemService = Depends(get_service)):
    try:
        return svc.get_item(item_id)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Item not found")


@router.put("/{item_id}", response_model=Item, summary="Update an item by id")
def update_item(
    item_id: int,
    payload: ItemUpdate,     # Important: Do NOT use = None
    svc: ItemService = Depends(get_service)
):
    try:
        return svc.update_item(item_id, payload.dict(exclude_none=True))
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/{item_id}", status_code=204, summary="Delete an item")
def delete_item(item_id: int, svc: ItemService = Depends(get_service)):
    try:
        svc.delete_item(item_id)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Item not found")
