from src.repositories.user_repository import UserRepository

def get_user_by_id(user_id: int, repo: UserRepository):
    """
    Business logic to fetch a user
    """
    user = repo.get_user(user_id)
    if not user:
        return None
    return user
