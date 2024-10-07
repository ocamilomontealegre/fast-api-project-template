from fastapi import FastAPI
from injector import Injector
from app.app_module import AppModule
from app.routers.app_router import AppRouter
from common.middleware import HTTPLoggingMiddleware


class AppBuilder:
    def __init__(self):
        self.__app = FastAPI()
        self.__injector = Injector([AppModule])
        self.__router = AppRouter(self.__injector).get_router()

    def set_http_logging_middleware(self) -> "AppBuilder":
        self.__app.add_middleware(HTTPLoggingMiddleware)
        return self

    def set_router(self) -> "AppBuilder":
        self.__app.include_router(self.__router, prefix="/api/v1", tags=["App"])
        return self

    def build(self):
        return self.__app
