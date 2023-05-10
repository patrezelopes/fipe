import logging
from contextlib import contextmanager
from typing import Generator

from pymongo import MongoClient

from app import settings

logger = logging.getLogger(__name__)


@contextmanager
def get_db_client() -> Generator[None, None, None]:
    mongodb_client = MongoClient(settings.MONGO_URI)
    try:
        yield mongodb_client
    except Exception as e:
        logger.error(f'get_db_client: {str(e)}')
        raise
    finally:
        mongodb_client.close()
