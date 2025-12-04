# app/core/db.py
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
MONGO_DB = "chartflow_dev"

client = None
db = None

async def connect_to_mongo():
    global client, db
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[MONGO_DB]
    print("MongoDB connected")

async def close_mongo_connection():
    global client
    client.close()
    print("MongoDB connection closed")
