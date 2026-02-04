from fastapi import APIRouter, UploadFile, File, Response
from src.services.file_service import FileService

router = APIRouter(prefix="/files", tags=["Files"])
service = FileService()

@router.post(
    "",
    summary="Upload a file",
    description="Uploads a file with size and type validation"
)
def upload_file(file: UploadFile = File(...)):
    return service.upload(file)

@router.get(
    "/{file_path}",
    summary="Download a file",
    description="Securely download file by ID"
)
def download_file(file_path: str):
    content = service.download(file_path)
    return Response(
        content,
        media_type="application/octet-stream",
        headers={
            "Content-Disposition": f'attachment; filename="{file_path}"'
        }
    )
