from fastapi.encoders import jsonable_encoder

from app import settings
from app.repository import get_db_client
from app.schemas.brand import BrandCreateSchema, BrandSchema


class BrandCollectionRepository:

    @staticmethod
    def insert(brand: BrandCreateSchema):
        with get_db_client() as db_client:
            db_client = db_client["fipe_db"]
            brands_collection = db_client['brands']
            if not brands_collection.find_one({"code": brand.code}):
                brands_collection.insert_one(jsonable_encoder(brand))

    @staticmethod
    def find_one(brand: BrandCreateSchema):
        with get_db_client() as db_client:
            db_client = db_client[settings.DB_NAME]
            brands_collection = db_client['brands']
            brand = brands_collection.find_one({"code": brand.code})
        return BrandSchema(**brand)

    @staticmethod
    def find():
        with get_db_client() as db_client:
            db_client = db_client[settings.DB_NAME]
            brands_collection = db_client['brands']
            brands = [BrandSchema(**brand) for brand in brands_collection.find()]
        return brands
