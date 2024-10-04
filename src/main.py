from fastapi import FastAPI
from injector import Injector
from uvicorn import run
from app.app_module import AppModule
from app.routers.app_router import AppRouter

def create_app() -> FastAPI:
    app = FastAPI()

    injector = Injector([AppModule()])

    router = AppRouter(injector)
    app.include_router(router.get_router(), prefix="/api/v1", tags=["App"])

    return app

app = create_app()

if __name__ == "__main__":
    # Start the server using Uvicorn
    run("main:app", host="127.0.0.1", port=8000, reload=True)