from fastapi import APIRouter
from injector import Injector
from health.controllers.health_controller import HealthController


class AppRouter:
    def __init__(self, injector: Injector):
        self._router = APIRouter()
        self._injector = injector
        self.register_routes()

    def register_routes(self):
        health_controller = self._injector.get(HealthController)

        self._router.include_router(health_controller.get_router(), prefix="/health")

    def get_router(self) -> APIRouter:
        return self._router
