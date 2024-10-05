from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppEnvVariables(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

    app_port: int = Field(default=8000)

    @field_validator("app_port")
    def validate_app_port(cls, v):
        if not (v <= 0 or v <= 65365):
            raise ValueError("app port must be between 0 and 65535")
        return v


def getAppEnvVariables() -> AppEnvVariables:
    return AppEnvVariables()


if __name__ == "__main":
    try:
        app_env = AppEnvVariables()
        print(f"Application will run on port: {app_env.app_port}")
    except ValueError as e:
        print(f"Error in environment variables: {e}")
