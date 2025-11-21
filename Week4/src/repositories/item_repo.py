from pathlib import Path
import json
from datetime import datetime, UTC
from threading import Lock
from typing import List, Dict, Optional


class ItemRepository:
    """Persist items to a JSON file with an in-memory cache."""

    def __init__(self, data_file: Path = Path("data/items.json")):
        self._file = data_file
        self._lock = Lock()

        # Ensure folder exists
        if not self._file.parent.exists():
            self._file.parent.mkdir(parents=True, exist_ok=True)

        # Ensure file exists
        if not self._file.exists():
            self._file.write_text("[]", encoding="utf-8")

        self._load()

    def _load(self):
        with self._lock:
            try:
                raw = self._file.read_text(encoding="utf-8")
                self._items: List[Dict] = json.loads(raw or "[]")
            except Exception:
                self._items = []

    def _save(self):
        with self._lock:
            self._file.write_text(
                json.dumps(self._items, default=str, indent=2),
                encoding="utf-8"
            )

    def _next_id(self) -> int:
        if not self._items:
            return 1
        return max(item["id"] for item in self._items) + 1

    def list(self) -> List[Dict]:
        return list(self._items)

    def get(self, item_id: int) -> Optional[Dict]:
        for item in self._items:
            if item["id"] == item_id:
                return dict(item)
        return None

    def create(self, payload: Dict) -> Dict:
        now = datetime.now(UTC).isoformat()
        item = dict(payload)
        item["id"] = self._next_id()
        item["created_at"] = now
        item["updated_at"] = now

        self._items.append(item)
        self._save()
        return dict(item)

    def update(self, item_id: int, payload: Dict) -> Optional[Dict]:
        for idx, item in enumerate(self._items):
            if item["id"] == item_id:
                updated = dict(item)

                # Apply only non-None values
                for k, v in payload.items():
                    if v is not None:
                        updated[k] = v

                updated["updated_at"] = datetime.now(UTC).isoformat()
                self._items[idx] = updated
                self._save()
                return dict(updated)

        return None

    def delete(self, item_id: int) -> bool:
        for idx, item in enumerate(self._items):
            if item["id"] == item_id:
                del self._items[idx]
                self._save()
                return True
        return False

    def search(self, q: Optional[str] = None) -> List[Dict]:
        if not q:
            return self.list()

        q_lower = q.lower()
        return [
            it
            for it in self._items
            if q_lower in (it.get("name", "").lower() + " " + it.get("description", "").lower())
        ]
