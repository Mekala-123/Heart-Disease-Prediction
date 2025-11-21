from typing import List, Any, Dict

def paginate(data: List[Any], page: int = 1, size: int = 10) -> Dict[str, Any]:
    if page < 1:
        page = 1
    if size < 1:
        size = 10

    total = len(data)
    start = (page - 1) * size
    end = start + size

    return {
        "page": page,
        "size": size,
        "total": total,
        "items": data[start:end],
    }
