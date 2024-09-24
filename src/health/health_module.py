from injector import Module, Binder, singleton
from health.services.health_service import HealthService

class HealthModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(HealthService, to=HealthService, scope=singleton)