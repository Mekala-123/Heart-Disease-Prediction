from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging

logger = logging.getLogger(__name__)


def error_response(
    status_code: int,
    message: str,
    trace_id: str | None = None
):
    return JSONResponse(
        status_code=status_code,
        content={
            "error": message,
            "trace_id": trace_id
        }
    )


# 🔹 Handles 401, 403, 404, 409 (HTTPException)
async def http_exception_handler(
    request: Request,
    exc: StarletteHTTPException
):
    trace_id = getattr(request.state, "trace_id", None)

    logger.warning(
        "HTTP exception",
        extra={
            "status_code": exc.status_code,
            "path": request.url.path,
            "trace_id": trace_id
        }
    )

    return error_response(
        status_code=exc.status_code,
        message=exc.detail,
        trace_id=trace_id
    )


# 🔹 Handles 400 (Validation errors)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    trace_id = getattr(request.state, "trace_id", None)

    logger.warning(
        "Validation error",
        extra={
            "errors": exc.errors(),
            "path": request.url.path,
            "trace_id": trace_id
        }
    )

    return error_response(
        status_code=status.HTTP_400_BAD_REQUEST,
        message="Invalid request data",
        trace_id=trace_id
    )


# 🔹 Handles 500 (Unhandled errors)
async def internal_exception_handler(
    request: Request,
    exc: Exception
):
    trace_id = getattr(request.state, "trace_id", None)

    logger.error(
        "Unhandled exception",
        exc_info=True,
        extra={
            "path": request.url.path,
            "trace_id": trace_id
        }
    )

    return error_response(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        message="Internal server error",
        trace_id=trace_id
    )
