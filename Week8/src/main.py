from fastapi import FastAPI
from src.api.users import router as users_router
from src.api.items import router as items_router


app = FastAPI(title="Week 8 – Authorization (RBAC)")

app.include_router(users_router)
app.include_router(items_router)
