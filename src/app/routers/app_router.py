from fastapi import APIRouter
from health.controllers.health_controller import HealthController


class AppRouter:
    def __init__(self):
        self.router = APIRouter()

        self.router.include_router(HealthController().router, prefix="/v1", tags=["Health"])

    def get_router(self) -> APIRouter:
        return self.router