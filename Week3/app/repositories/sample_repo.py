class SampleRepository:
    def __init__(self):
        self.data = []

    def get_by_id(self, id: int):
        return {"id": id, "name": "data from repo"}

    def save(self, item: dict):
        self.data.append(item)
        item["id"] = len(self.data)   # Assign fake ID
        return item
