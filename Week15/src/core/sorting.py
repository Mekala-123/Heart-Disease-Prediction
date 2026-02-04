from sqlalchemy.orm import Query

def apply_sorting(query: Query, model, sort: str) -> Query:
    if not sort:
        return query

    field_name = sort.lstrip("-")
    field = getattr(model, field_name, None)

    if field is None:
        return query

    return query.order_by(field.desc() if sort.startswith("-") else field.asc())
