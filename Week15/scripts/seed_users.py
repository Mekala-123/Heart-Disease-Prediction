# scripts/seed_users.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from src.core.database import SessionLocal, Base
from src.models.user import User
from sqlalchemy.orm import Session

# Create tables if not exists
Base.metadata.create_all(bind=SessionLocal.kw["bind"])

# Create session
db: Session = SessionLocal()

users = [
    User(name="John", email="john@test.com"),
    User(name="Jane", email="jane@test.com"),
    User(name="Python Dev", email="python@test.com"),
]

db.add_all(users)
db.commit()
db.close()

print("Seed data inserted")
