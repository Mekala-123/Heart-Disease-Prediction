from src.core.security import hash_password, verify_password, create_token, decode_token

_USERS = {}   # temporary in-memory DB

def register_user(email, password):
    if email in _USERS:
        raise ValueError("exists")

    _USERS[email] = {
        "email": email,
        "hash": hash_password(password),
        "roles": ["user"]
    }
    return _USERS[email]

def authenticate(email, password):
    user = _USERS.get(email)
    if not user:
        return None
    if not verify_password(password, user["hash"]):
        return None
    return user

def create_tokens(email):
    access = create_token(email, "access", expires=900)        # 15 min
    refresh = create_token(email, "refresh", expires=604800)   # 7 days
    return {"access_token": access, "refresh_token": refresh}

def refresh_token(refresh_token):
    payload = decode_token(refresh_token)
    if payload["type"] != "refresh":
        raise ValueError("bad_refresh")
    email = payload["sub"]
    return create_tokens(email)