from pydantic import BaseModel
from uuid import UUID

class FileMeta(BaseModel):
    id: UUID
    filename: str
    content_type: str
    size: int
    path: str
