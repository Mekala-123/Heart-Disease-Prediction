from fastapi import FastAPI
from app.core.db import connect_to_mongo, close_mongo_connection
from app.routers.item_router import router as item_router

app = FastAPI(title="Week5 MongoDB Integration")

@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()  # Initialize MongoDB

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

app.include_router(item_router)
