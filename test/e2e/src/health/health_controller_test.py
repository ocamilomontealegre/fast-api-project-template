import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from src.health.controllers.health_controller import HealthController
from src.health.services.health_service import HealthService


@pytest.fixture
def app() -> FastAPI:
    app = FastAPI()
    health_service = HealthService()
    health_controller = HealthController(health_service)
    app.include_router(health_controller.get_router(), prefix="/api/v1/health")
    return app


@pytest.fixture
def client(app: FastAPI) -> TestClient:
    """Create a TestClient for the app"""
    return TestClient(app)


def test_health_check(client: TestClient):
    """Test the health check endpoint for a successful response."""
    response = client.get("/api/v1/health")

    assert response.status_code == 200
