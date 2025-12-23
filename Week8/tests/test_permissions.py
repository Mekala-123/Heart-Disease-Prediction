import pytest
from fastapi import HTTPException
from src.core.permissions import require_role


def test_admin_allowed():
    checker = require_role(["admin"])
    user = {"roles": ["admin"]}
    assert checker(user) == user

def test_user_denied():
    checker = require_role(["admin"])
    user = {"roles": ["user"]}

    with pytest.raises(HTTPException) as exc:
        checker(user)

    assert exc.value.status_code == 403
