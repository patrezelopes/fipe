from pydantic import validator

from app.schemas import BaseCreateSchema, BaseUpdateSchema


class BrandCreateSchema(BaseCreateSchema):
    code: int
    name: str

    @validator("code", pre=True, always=True)
    def validate_code(cls, value: int | str) -> int:
        try:
            return int(value)
        except Exception:
            raise ValueError('passwords do not match')


class BrandUpdateSchema(BaseUpdateSchema):
    code: int
    name: str


class BrandSchema(BaseCreateSchema):
    code: int
    name: str
