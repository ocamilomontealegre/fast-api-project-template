from typing import Callable, Awaitable
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse, Response
from fastapi import Request
from common.loggers.logger import AppLogger


class HTTPLoggingInterceptor(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.__logger = AppLogger(log_level="DEBUG", label="OK")

    async def dispatch(
        self,
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:

        try:

            response = await call_next(request)
            self.__logger.info(
                f"incoming request: METHOD {request.method} | URL {request.url.path}",
                f"outgoing response: STATUS {response.status_code}",
            )

            return response

        except Exception as e:
            self.__logger.error(f"Unhandled error: {e}")
            self.__logger.exception(e)

            return JSONResponse({"detail": "Internal Server Error"}, status_code=500)
