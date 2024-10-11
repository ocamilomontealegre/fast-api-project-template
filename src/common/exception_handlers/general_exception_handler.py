from datetime import datetime, timezone
from fastapi import Request
from fastapi.responses import JSONResponse
from common.loggers.logger import AppLogger
from common.models import ResponseModel


class GeneralExceptionHandler:
    @staticmethod
    async def handle_exception(request: Request, exc: Exception) -> JSONResponse:
        logger = AppLogger(label=GeneralExceptionHandler.__name__)

        response = ResponseModel(
            status=500,
            success=False,
            message="Internal Server Error",
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

        logger.error(
            f"[INCOMING REQUEST] METHOD: {request.method} | URL: {request.url.path} | HEADERS: {request.headers} "
            f"[OUTGOING RESPONSE] STATUS: {response.status} | RESPONSE_BODY: {response}"
        )

        return JSONResponse(content=response.dict(), status_code=500)
