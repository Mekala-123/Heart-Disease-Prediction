from fastapi import Depends, HTTPException, status
from src.core.security import get_current_user


def require_role(required_roles: list[str]):
    """
    RBAC guard to restrict endpoint access by role.
    """
    def role_checker(user: dict = Depends(get_current_user)):
        user_roles = user.get("roles", [])

        if not any(role in user_roles for role in required_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Forbidden: insufficient permissions"
            )

        return user

    return role_checker
