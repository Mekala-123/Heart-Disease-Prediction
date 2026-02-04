from sqlalchemy.orm import Query
from sqlalchemy import or_

def apply_text_search(
    query: Query,
    model,
    search: str,
    fields: list[str]
) -> Query:
    if not search:
        return query

    conditions = [
        getattr(model, field).ilike(f"%{search}%")
        for field in fields
    ]

    return query.filter(or_(*conditions))
