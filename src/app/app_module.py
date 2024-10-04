from injector import Binder, Module
from health.health_module import HealthModule
from app.routers.app_router import AppRouter

class AppModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.install(HealthModule())