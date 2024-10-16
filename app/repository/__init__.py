import logging
from contextlib import contextmanager
from typing import Generator

from pymongo import MongoClient

from app import settings

logger = logging.getLogger(__name__)


@contextmanager
def get_db_client() -> Generator[None, None, None]:
    pass