from app.schemas import BaseCreateSchema, BaseUpdateSchema


class ModelCreateSchema(BaseCreateSchema):
    code: int
    brand: int
    name: str


class ModelRequestToCreateSchema(BaseCreateSchema):
    brand: int


class ModelUpdateSchema(BaseUpdateSchema):
    code: int
    brand: str
    name: str


class ModelSchema(BaseUpdateSchema):
    code: int
    brand: str
    name: str
