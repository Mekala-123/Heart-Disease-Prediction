# Mock DB
USERS_DB = [
    {"id": 1, "email": "admin@test.com", "roles": ["admin"]},
    {"id": 2, "email": "user1@test.com", "roles": ["user"]},
    {"id": 3, "email": "user2@test.com", "roles": ["user"]},
]

def get_users(offset: int, limit: int):
    return USERS_DB[offset : offset + limit]
