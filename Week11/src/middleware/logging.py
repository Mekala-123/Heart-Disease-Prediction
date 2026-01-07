# src/middleware/logging.py
import time
import uuid
import logging
from starlette.types import ASGIApp, Receive, Scope, Send

# Configure the logger (you can adjust format or handlers as needed)
logger = logging.getLogger("uvicorn.error")


class LoggingMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        if scope["type"] != "http":
            # Only handle HTTP requests
            await self.app(scope, receive, send)
            return

        start_time = time.time()
        trace_id = str(uuid.uuid4())
        response_sent = False

        async def send_wrapper(message):
            nonlocal response_sent
            if message["type"] == "http.response.start":
                if response_sent:
                    # Prevent multiple response starts
                    return
                response_sent = True
            await send(message)

        try:
            await self.app(scope, receive, send_wrapper)
        except Exception as exc:
            # Log exceptions
            logger.error({
                "level": "ERROR",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "path": scope.get("path"),
                "method": scope.get("method"),
                "status_code": getattr(exc, "status_code", 500),
                "user": "anonymous",
                "trace_id": trace_id,
                "duration": round(time.time() - start_time, 4),
                "error": str(exc),
            })
            raise  # Let FastAPI's error handler handle it
        finally:
            # Log request info (only if response_sent)
            duration = round(time.time() - start_time, 4)
            logger.info({
                "level": "INFO",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "path": scope.get("path"),
                "method": scope.get("method"),
                "status_code": 200 if response_sent else "unknown",
                "user": "anonymous",
                "trace_id": trace_id,
                "duration": duration,
            })
