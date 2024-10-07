from uvicorn import run
from app.app_builder import AppBuilder
from common.env.env_config import get_env_variables

app_env_variables = get_env_variables().app
app = AppBuilder().set_http_logging_middleware().set_router().build()

if __name__ == "__main__":
    run(
        "main:app",
        host=app_env_variables.host,
        port=app_env_variables.port,
        reload=True,
    )
