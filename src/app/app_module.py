from injector import Module
from health.health_module import HealthModule
from app.routers.app_router import AppRouter

class AppModule(Module):
    def __init__(self):
        self.router = AppRouter()

    def configure(self, binder):
        binder.install(HealthModule())

    def get_app_router(self) -> AppRouter:
        return self.router