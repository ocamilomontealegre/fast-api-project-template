from typing import Callable, Awaitable
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse, Response
from fastapi import Request
from loguru import logger


class HTTPLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self,
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        try:
            response = await call_next(request)
            logger.info(
                f"incoming request: METHOD {request.method} | URL {request.url.path}",
                f"outgoing response: STATUS {response.status_code}",
            )

            return response
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            logger.exception(e)
            return JSONResponse({"detail": "Internal Server Error"}, status_code=500)
