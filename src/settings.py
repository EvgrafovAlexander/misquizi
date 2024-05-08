# thirdparty
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8888

    model_config = SettingsConfigDict(env_file=".env", extra='ignore')
