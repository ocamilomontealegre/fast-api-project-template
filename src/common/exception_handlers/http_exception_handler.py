from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from common.loggers.logger import AppLogger
from common.utils import extract_exception_details
from common.models import HTTPResponse


class HTTPExceptionHandler:
    @staticmethod
    async def handle_exception(
        request: Request, exc: HTTPException
    ) -> JSONResponse:
        logger = AppLogger(label=HTTPExceptionHandler.__name__)

        exception_details = extract_exception_details(exc)

        response = HTTPResponse(
            status=exc.status_code,
            success=False,
            message=exc.detail,
        )

        logger.error(
            f"[INCOMING REQUEST] METHOD: {request.method} | URL: {request.url.path} | HEADERS: {request.headers} "
            f"[OUTGOING RESPONSE] STATUS: {response.status} | RESPONSE_BODY: {response} | EXCEPTION: {exception_details}"
        )

        return JSONResponse(
            content=response.dict(), status_code=exc.status_code
        )
