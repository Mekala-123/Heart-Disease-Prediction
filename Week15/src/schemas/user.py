from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # replace old Config class

    id: int
    name: str
    email: str
    created_at: datetime
