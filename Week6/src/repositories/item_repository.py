# src/repositories/item_repository.py

from typing import List
# src/repositories/item_repository.py
from src.schemas.item_dto import ItemCreateDTO, ItemResponseDTO

class ItemRepository:
    def __init__(self):
        self.items = []
        self.counter = 1  # auto-increment id

    def create(self, item_dto: ItemCreateDTO) -> ItemResponseDTO:
        item = ItemResponseDTO(
            id=self.counter,
            name=item_dto.name,
            description=item_dto.description
        )
        self.items.append(item)
        self.counter += 1
        return item

    def exists_by_name(self, name: str) -> bool:
        return any(item.name == name for item in self.items)

    def list_all(self):
        return self.items

    def get_by_id(self, item_id: int):
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def update(self, item_id: int, item_dto):
        item = self.get_by_id(item_id)
        if item:
            item.name = item_dto.name or item.name
            item.description = item_dto.description or item.description
        return item

    def delete(self, item_id: int):
        self.items = [item for item in self.items if item.id != item_id]
