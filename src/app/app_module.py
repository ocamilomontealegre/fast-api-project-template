from injector import Module
from health.health_module import HealthModule

class AppModule(Module):
    def configure(self, binder):
        binder.install(HealthModule())