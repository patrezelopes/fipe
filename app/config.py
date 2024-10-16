import os

from pydantic import BaseSettings, AnyUrl, MongoDsn

from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Settings(BaseSettings):
    project_name = os.environ.get("PROJECT_NAME", "fipe")
    api_version = os.environ.get("API_VERSION", "")
    environment: str = os.environ.get("ENV", "dev")
    version: str = os.environ.get("VERSION", "0.1.0")
    debug: bool = config('DEBUG', default=True, cast=bool)
    log_level: str = os.environ.get("LOG_LEVEL", "INFO")
    fipe_base_url: str = os.environ.get("FIPE_URL", "http://localhost:8000/fipe/")
    api_path: str = os.environ.get("API_PATH", "/")
    backend_cors_origins = os.environ.get("BACKEND_CORS_ORIGINS", "*")
    OPERATIONS_HOST: AnyUrl = "http://localhost:8000"
    API_KEY: str = "1111"
    AUTHORIZATION: str = "code"

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "[%(asctime)s][%(levelname)s] %(name)s "
                          "%(filename)s:%(funcName)s:%(lineno)d | %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
        "handlers": {
            "default": {
                "level": log_level,
                "formatter": "standard",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            "": {
                "handlers": ["default"],
                "level": log_level,
                "propagate": False,
            },
        },
    }

    class Config:
        env_file = ".env"


settings = Settings()
