from sqlalchemy.orm import Query
from typing import Optional
from sqlalchemy.sql import ColumnElement

def apply_offset_pagination(
    query: Query,
    page: int = 1,
    limit: int = 10
) -> Query:
    offset = (page - 1) * limit
    return query.offset(offset).limit(limit)


def apply_cursor_pagination(
    query: Query,
    cursor: Optional[int],
    cursor_field: ColumnElement,
    limit: int = 10
) -> Query:
    if cursor:
        query = query.filter(cursor_field > cursor)
    return query.order_by(cursor_field).limit(limit)
