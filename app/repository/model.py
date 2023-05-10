from fastapi.encoders import jsonable_encoder

from app import settings
from app.repository import get_db_client
from app.schemas.model import ModelCreateSchema, ModelSchema


class ModelCollectionRepository:

    @staticmethod
    def insert(model: ModelCreateSchema):
        with get_db_client() as db_client:
            db_client = db_client[settings.DB_NAME]
            models_collection = db_client['models']
            if not models_collection.find_one({"code": model.code}):
                models_collection.insert_one(jsonable_encoder(model))

    @staticmethod
    def find_one(model: ModelCreateSchema):
        with get_db_client() as db_client:
            db_client = db_client["fipe_db"]
            models_collection = db_client['brands']
            brand = models_collection.find_one({"code": model.code})
        return brand

    @staticmethod
    def find(model: ModelCreateSchema):
        with get_db_client() as db_client:
            db_client = db_client["fipe_db"]
            models_collection = db_client['brands']
            brands = [ModelSchema(model) for model in models_collection.find({"code": model.code})]
        return brands
