from datetime import datetime, timezone
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from common.loggers.logger import AppLogger
from common.models.http_response_model import ResponseModel


class HTTPExceptionHandler:
    @staticmethod
    async def handle_exception(request: Request, exc: HTTPException) -> JSONResponse:
        logger = AppLogger(label=HTTPExceptionHandler.__name__)

        response = ResponseModel(
            status=exc.status_code,
            success=False,
            message=exc.detail,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

        logger.error(
            f"[INCOMING REQUEST] METHOD: {request.method} | URL: {request.url.path} | HEADERS: {request.headers} "
            f"[OUTGOING RESPONSE] STATUS: {response.status} | RESPONSE_BODY: {response}"
        )

        return JSONResponse(content=response.dict(), status_code=exc.status_code)
