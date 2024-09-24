from fastapi import FastAPI
from injector import Injector
from uvicorn import run
from app.app_module import AppModule
from health.controllers.health_controller import HealthController

def create_app() -> FastAPI:
    app = FastAPI()

    # Initialize the DI container with the AppModule
    injector = Injector([AppModule()])

    # Inject the HealthController with dependencies resolved
    health_controller = injector.get(HealthController)

    # Include the controller's router in the app
    app.include_router(health_controller.router, prefix="/v1", tags=["Health"])

    return app

app = create_app()

if __name__ == "__main__":
    # Start the server using Uvicorn
    run("main:app", host="127.0.0.1", port=8000, reload=True)