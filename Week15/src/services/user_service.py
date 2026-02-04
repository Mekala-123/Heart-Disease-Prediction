from sqlalchemy.orm import Session
from src.models.user import User
from src.core.pagination import (
    apply_offset_pagination,
    apply_cursor_pagination
)
from src.core.sorting import apply_sorting
from src.core.search import apply_text_search

def get_users(
    db: Session,
    page: int,
    limit: int,
    cursor: int | None,
    sort: str | None,
    q: str | None
):
    query = db.query(User)

    # Search
    query = apply_text_search(query, User, q, ["name", "email"])

    # Sorting
    query = apply_sorting(query, User, sort or "-created_at")

    # Pagination
    if cursor:
        query = apply_cursor_pagination(query, cursor, User.id, limit)
    else:
        query = apply_offset_pagination(query, page, limit)

    # Projection
    return query.with_entities(
        User.id,
        User.name,
        User.email,
        User.created_at
    ).all()
