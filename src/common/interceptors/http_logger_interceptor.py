from typing import Callable, Awaitable
from datetime import datetime, timezone
from json import loads
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse, Response
from fastapi import FastAPI, Request
from common.loggers.logger import AppLogger
from common.models.http_response_model import ResponseModel


class HTTPLoggingInterceptor(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)
        self.__logger = AppLogger(log_level="INFO", label=self.__class__.__name__)

    async def __format_response(self, response: Response) -> ResponseModel:
        response_body = [section async for section in response.body_iterator]
        response_body_str = b"".join(response_body).decode("utf-8")
        data = loads(response_body_st)

        return ResponseModel(
            status=response.status_code,
            success=response.status_code == 200,
            message="OK",
            data=data,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

    async def dispatch(
        self,
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:

        response = await call_next(request)

        if response.status_code < 400:
            formated_response = await self.__format_response(response)
            self.__logger.info(
                f"[INCOMING REQUEST] METHOD: {request.method} | URL: {request.url.path} | HEADERS: {request.headers} "
                f"[OUTGOING RESPONSE] STATUS: {response.status_code} | RESPONSE_BODY: {formated_response.data}"
            )

            return JSONResponse(
                content=formated_response.dict(), status_code=response.status_code
            )

        return response

    # except Exception as e:
    #     # Log your custom error message here
    #     self.__logger.error(f"Error in HTTPLoggingInterceptor: {str(e)}")
    #     # You can return an error response or re-raise the error
    #     return JSONResponse({"detail": "Internal Server Error"}, status_code=500)
