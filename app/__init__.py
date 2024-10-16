import logging
import logging.config
from dotenv import dotenv_values
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.config import settings
from app.core.containers import Container
from app.routers.urls import api_router
from app.config import settings

logger = logging.getLogger(__name__)


config = dotenv_values(".env")


def create_app() -> FastAPI:
    container = Container()
    app = FastAPI(
        title=settings.project_name,
        debug=settings.debug,
        root_path=settings.api_path,
        enviroment=settings.environment,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix=settings.api_version)

    logging.config.dictConfig(settings.LOGGING)
    logger.info(f"starting app {settings.project_name}")

    return app
