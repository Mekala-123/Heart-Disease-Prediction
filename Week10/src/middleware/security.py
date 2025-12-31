# src/middleware/security.py
import time
from typing import Callable
from fastapi import Request, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from src.core.config import settings
from src.core.redis import redis_client


def setup_cors(app) -> None:
    """
    Configure CORS using allowed origins from config.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


class RateLimiterMiddleware(BaseHTTPMiddleware):
    """
    Redis-based sliding window rate limiter middleware.
    """

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        client_ip = request.client.host
        key = f"rate:{client_ip}"
        now = int(time.time())

        pipe = redis_client.pipeline()
        pipe.zadd(key, {now: now})
        pipe.zremrangebyscore(key, 0, now - settings.RATE_LIMIT_WINDOW)
        pipe.zcard(key)
        pipe.expire(key, settings.RATE_LIMIT_WINDOW)
        _, _, request_count, _ = pipe.execute()

        if request_count > settings.RATE_LIMIT_REQUESTS:
            raise HTTPException(status_code=429, detail="Too many requests")

        return await call_next(request)


class RequestSizeLimiterMiddleware(BaseHTTPMiddleware):
    """
    Reject requests exceeding configured size limit.
    Works for JSON payloads by recreating request stream.
    """

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        body = await request.body()
        if len(body) > settings.MAX_REQUEST_SIZE:
            raise HTTPException(status_code=413, detail="Request too large")

        # Recreate request stream so downstream endpoints can read JSON
        async def receive():
            return {"type": "http.request", "body": body}
        request._receive = receive

        return await call_next(request)


class SecureHeadersMiddleware(BaseHTTPMiddleware):
    """
    Add secure HTTP response headers.
    """

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=63072000"
        return response
