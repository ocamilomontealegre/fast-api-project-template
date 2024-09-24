from fastapi import APIRouter
from injector import inject
from health.services.health_service import HealthService

class HealthController:
    @inject
    def __init__(self, health_service: HealthService):
        self._health_service = health_service
        self._router = APIRouter()

        @self._router.get("/health")
        def check():
            return self._health_service.check()
        
    @property
    def router(self):
        return self._router