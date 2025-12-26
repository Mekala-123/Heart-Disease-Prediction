from typing import List, Dict

# Fake DB for demo
_ITEMS_DB: List[Dict] = [
    {"id": 1, "name": "Item A"},
    {"id": 2, "name": "Item B"}
]

def get_all_items() -> List[Dict]:
    return _ITEMS_DB

def get_item_by_id(item_id: int) -> Dict | None:
    for item in _ITEMS_DB:
        if item["id"] == item_id:
            return item
    return None

def create_item(item: Dict) -> Dict:
    _ITEMS_DB.append(item)
    return item
