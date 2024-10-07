from pydantic import BaseModel, Field


class AppEnvVariables(BaseModel):
    host: str = Field(default="localhost", description="App server host")
    port: int = Field(ge=0, le=65535, default=8000, description="App server port")
