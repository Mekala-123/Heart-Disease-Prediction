from app.repositories.sample_repo import SampleRepository

class SampleService:
    def __init__(self):
        self.repo = SampleRepository()

    def get_sample(self, id: int):
        data = self.repo.get_by_id(id)

        return {
            "id": data["id"],
            "name": data["name"],
            "source": "service-layer"
        }

    def create_sample(self, item):
        saved = self.repo.save(item)
        return {"message": "Sample Created", "data": saved}
