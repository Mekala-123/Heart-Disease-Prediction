from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    email = Column(String)
    age = Column(Integer)
