import json
from src.repositories.item_repository import (
    get_all_items,
    get_item_by_id,
    create_item
)
from src.services.cache_service import (
    get_cache,
    set_cache,
    invalidate_cache
)
from src.core.config import ROUTE_TTL


def fetch_items():
    cache_key = "items:list"
    cached = get_cache(cache_key)

    if cached:
        return json.loads(cached)

    data = get_all_items()
    set_cache(cache_key, json.dumps(data), ROUTE_TTL["items_list"])
    return data


def fetch_item(item_id: int):
    cache_key = f"items:{item_id}"
    cached = get_cache(cache_key)

    if cached:
        return json.loads(cached)

    item = get_item_by_id(item_id)
    if item:
        set_cache(cache_key, json.dumps(item), ROUTE_TTL["item_by_id"])
    return item


def add_item(item: dict):
    invalidate_cache("items:*")
    return create_item(item)
