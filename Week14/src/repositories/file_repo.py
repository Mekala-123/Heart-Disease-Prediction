import os
from uuid import uuid4
from src.core.config import UPLOAD_DIR

class FileRepository:

    def save(self, file_bytes: bytes, filename: str) -> dict:
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        file_id = uuid4()
        stored_name = f"{file_id}_{filename}"
        full_path = os.path.join(UPLOAD_DIR, stored_name)

        with open(full_path, "wb") as f:
            f.write(file_bytes)

        return {
            "file_id": str(file_id),
            "stored_name": stored_name
        }

    def get(self, stored_name: str) -> bytes:
        # Prevent path traversal
        if ".." in stored_name or "/" in stored_name or "\\" in stored_name:
            raise FileNotFoundError()

        full_path = os.path.join(UPLOAD_DIR, stored_name)

        if not os.path.exists(full_path):
            raise FileNotFoundError()

        with open(full_path, "rb") as f:
            return f.read()
