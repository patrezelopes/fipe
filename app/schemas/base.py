from uuid import UUID, uuid4
from typing import Optional
from datetime import datetime

from pydantic import BaseModel, validator


class BaseCreateSchema(BaseModel):
    uuid: Optional[UUID]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted: Optional[bool]

    @validator("created_at", "updated_at", pre=True, always=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.now()

    @validator("uuid", pre=True, always=True)
    def default_uuid(cls, value: UUID) -> UUID:
        return value or uuid4()

    @validator("deleted", pre=True, always=True)
    def default_deleted(cls, value: bool) -> bool:
        return value or False

    class Config:
        orm_mode = True


class BaseUpdateSchema(BaseModel):
    uuid: UUID
    updated_at: Optional[datetime]
    deleted: Optional[bool]

    @validator("updated_at", pre=True, always=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.now()

    class Config:
        orm_mode = True
        