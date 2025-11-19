from fastapi import APIRouter, Depends
from app.schemas.sample import SampleCreate, SampleResponse
from app.services.sample_service import SampleService

router = APIRouter()

def get_service():
    return SampleService()

@router.get("/sample/{id}", response_model=SampleResponse)
def get_sample(id: int, service: SampleService = Depends(get_service)):
    return service.get_sample(id)

@router.post("/sample")
def create_sample(item: SampleCreate, service: SampleService = Depends(get_service)):
    return service.create_sample(item.dict())
