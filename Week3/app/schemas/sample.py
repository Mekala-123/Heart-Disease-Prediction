from pydantic import BaseModel

class SampleCreate(BaseModel):
    name: str
    age: int

class SampleResponse(BaseModel):
    id: int
    name: str
    source: str
