from fastapi.encoders import jsonable_encoder

from app import settings
from app.repository import get_db_client
from app.schemas.brand import BrandCreateSchema, BrandSchema


class BrandCollectionRepository:

    @staticmethod
    def insert(brand: BrandCreateSchema):
        pass

    @staticmethod
    def find_one(brand: BrandCreateSchema):
        pass

    @staticmethod
    def find():
        pass