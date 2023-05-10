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
    parallelum_base_url: str = os.environ.get("PARALLELUM_URL", "https://parallelum.com.br/fipe/api/v1/")
    fipe_base_url: str = os.environ.get("FIPE_URL", "http://localhost:8000/fipe/")
    api_path: str = os.environ.get("API_PATH", "/")
    backend_cors_origins = os.environ.get("BACKEND_CORS_ORIGINS", "*")
    MONGO_URI: MongoDsn = os.environ.get("MONGO_URI", "")
    DB_NAME: str = os.environ.get("DB_NAME", "")
    OPERATIONS_HOST: AnyUrl = "http://localhost:8000"
    API_KEY: str = "1111"
    AUTHORIZATION: str = "code"
    BROKER_URL = "amqp://rabbitmq:5672"
    BROKER_HOST: str = os.environ.get("BROKER_HOST", "localhost")
    BROKER_USER: str = os.environ.get("BROKER_USER", "guest")
    BROKER_PASS: str = os.environ.get("BROKER_PASS", "guest")
    BROKER_PORT: int = os.environ.get("BROKER_PORT", 5672)
    BRANDS_QUEUE: str = os.environ.get("BRANDS_QUEUE", "brands_events_queue")
    MODELS_QUEUE: str = os.environ.get("MODELS_QUEUE", "models_events_queue")
    BRANDS_ROUTING_KEY: str = os.environ.get("BRANDS_ROUTING_KEY", "brands")
    MODELS_ROUTING_KEY: str = os.environ.get("MODELS_ROUTING_KEY", "models")
    V_HOST: str = os.environ.get("V_HOST", "/")

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
