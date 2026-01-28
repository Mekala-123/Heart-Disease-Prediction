import asyncio

async def external_call():
    await asyncio.sleep(5)
    return {"linkedin": "profile-url"}

async def safe_external_call():
    try:
        return await asyncio.wait_for(external_call(), timeout=2)
    except asyncio.TimeoutError:
        return {"error": "Timeout"}
