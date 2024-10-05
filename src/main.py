from fastapi import FastAPI
from injector import Injector
from uvicorn import run
from app.app_module import AppModule
from app.routers.app_router import AppRouter
from common.middleware.http_logger_middleware import HTTPLoggingMiddleware
from common.env.app_config import getAppEnvVariables

appVariables = getAppEnvVariables()


def create_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(HTTPLoggingMiddleware)

    injector = Injector([AppModule()])

    router = AppRouter(injector)
    app.include_router(router.get_router(), prefix="/api/v1", tags=["App"])

    return app


app = create_app()

if __name__ == "__main__":
    run(
        "main:app",
        host="127.0.0.1",
        port=appVariables.app_port,
        reload=True,
        log_level="info",
    )
