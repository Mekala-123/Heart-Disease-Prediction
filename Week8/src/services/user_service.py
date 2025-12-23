from src.repositories.user_repository import get_users


def list_users(page: int, size: int):
    offset = (page - 1) * size
    return get_users(offset, size)
