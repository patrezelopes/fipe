from fastapi.encoders import jsonable_encoder

from app import settings
from app.repository import get_db_client
from app.schemas.model import ModelCreateSchema, ModelSchema


class ModelCollectionRepository:

    @staticmethod
    def insert(model: ModelCreateSchema):
        pass

    @staticmethod
    def find_one(model: ModelCreateSchema):
        pass

    @staticmethod
    def find(model: ModelCreateSchema):
        pass
