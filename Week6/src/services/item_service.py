# src/services/item_service.py
from src.schemas.item_dto import ItemCreateDTO, ItemUpdateDTO, ItemResponseDTO
from src.core.errors import NotFoundError, ConflictError, ValidationError

class ItemService:
    def __init__(self, repo):
        self.repo = repo

    def create_item(self, item_dto: ItemCreateDTO) -> ItemResponseDTO:
        if self.repo.exists_by_name(item_dto.name):
            raise ConflictError(f"Item with name '{item_dto.name}' already exists")
        return self.repo.create(item_dto)

    def list_items(self):
        return self.repo.list_all()

    def get_item(self, item_id: int):
        item = self.repo.get_by_id(item_id)
        if not item:
            raise NotFoundError(f"Item with id {item_id} not found")
        return item

    def update_item(self, item_id: int, item_dto: ItemUpdateDTO):
        item = self.repo.update(item_id, item_dto)
        if not item:
            raise NotFoundError(f"Item with id {item_id} not found")
        return item

    def delete_item(self, item_id: int):
        item = self.repo.get_by_id(item_id)
        if not item:
            raise NotFoundError(f"Item with id {item_id} not found")
        self.repo.delete(item_id)
