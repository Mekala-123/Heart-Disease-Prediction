# src/routers/item_router.py
from fastapi import APIRouter, HTTPException
from src.services.item_service import ItemService
from src.repositories.item_repository import ItemRepository
from src.schemas.item_dto import ItemCreateDTO, ItemUpdateDTO, ItemResponseDTO
from src.core.errors import NotFoundError, ConflictError, ValidationError

router = APIRouter(prefix="/items", tags=["Items"])  # add prefix and tags
repo = ItemRepository()
service = ItemService(repo)

# CREATE
@router.post("/", response_model=ItemResponseDTO)
def create_item(item: ItemCreateDTO):
    try:
        return service.create_item(item)
    except ConflictError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

# LIST ALL
@router.get("/", response_model=list[ItemResponseDTO])
def list_items():
    return service.list_items()

# GET SINGLE
@router.get("/{item_id}", response_model=ItemResponseDTO)
def get_item(item_id: int):
    try:
        return service.get_item(item_id)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

# UPDATE
@router.put("/{item_id}", response_model=ItemResponseDTO)
def update_item(item_id: int, item: ItemUpdateDTO):
    try:
        return service.update_item(item_id, item)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ConflictError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

# DELETE
@router.delete("/{item_id}")
def delete_item(item_id: int):
    try:
        service.delete_item(item_id)
        return {"message": "Item deleted successfully"}
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
