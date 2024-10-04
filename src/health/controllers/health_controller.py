from fastapi import APIRouter
from injector import inject
from health.services.health_service import HealthService

class HealthController:
    @inject
    def __init__(self, health_service: HealthService):
        self._health_service = health_service
        self._router = APIRouter()
        self._register_routes()
    
    def _register_routes(self):
        @self._router.get("/")
        async def check():
            return self._health_service.check()
    
    def get_router(self) -> APIRouter:
        return self._router