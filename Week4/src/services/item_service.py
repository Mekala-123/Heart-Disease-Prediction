from typing import Optional, Dict, Any
from src.repositories.item_repo import ItemRepository
from src.core.pagination import paginate
from src.core.errors import NotFoundError


class ItemService:
    """Business logic and validation."""

    def __init__(self, repo: Optional[ItemRepository] = None):
        self.repo = repo or ItemRepository()

    def create_item(self, payload: Dict[str, Any]) -> Dict:
        payload = dict(payload)
        payload["name"] = payload.get("name", "").strip()

        if not payload["name"]:
            raise ValueError("name must not be empty")

        return self.repo.create(payload)

    def get_item(self, item_id: int) -> Dict:
        item = self.repo.get(item_id)
        if not item:
            raise NotFoundError(f"Item {item_id} not found")
        return item

    def list_items(self, q: Optional[str], page: int, size: int) -> Dict:
        results = self.repo.search(q)
        results.sort(key=lambda x: x["id"])
        return paginate(results, page=page, size=size)

    def update_item(self, item_id: int, payload: Dict) -> Dict:
        item = self.repo.update(item_id, payload)
        if not item:
            raise NotFoundError(f"Item {item_id} not found")
        return item

    def delete_item(self, item_id: int) -> None:
        ok = self.repo.delete(item_id)
        if not ok:
            raise NotFoundError(f"Item {item_id} not found")
