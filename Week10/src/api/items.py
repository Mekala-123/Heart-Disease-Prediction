from fastapi import APIRouter, Request

router = APIRouter()

items = ["item1", "item2"]

@router.get("/items/")
async def get_items():
    return {"items": items}

@router.post("/items/")
async def create_item(request: Request):
    data = await request.json()
    return {"received": len(data.get("data", ""))}

