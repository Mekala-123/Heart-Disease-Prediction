from fastapi import UploadFile, HTTPException
from src.core.config import MAX_FILE_SIZE, ALLOWED_CONTENT_TYPES
from src.repositories.file_repo import FileRepository

repo = FileRepository()

class FileService:

    def upload(self, file: UploadFile):
        # 1. Validate content type
        if file.content_type not in ALLOWED_CONTENT_TYPES:
            raise HTTPException(status_code=400, detail="Invalid file type")

        # 2. Read file safely
        file_bytes = file.file.read()

        if not file_bytes:
            raise HTTPException(status_code=400, detail="Empty file")

        # 3. Validate size
        if len(file_bytes) > MAX_FILE_SIZE:
            raise HTTPException(status_code=400, detail="File too large")

        # 4. Save
        stored = repo.save(file_bytes, file.filename)

        return {
            "file_id": stored["file_id"],
            "stored_name": stored["stored_name"]
        }

    def download(self, stored_name: str) -> bytes:
        try:
            return repo.get(stored_name)
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail="File not found")
