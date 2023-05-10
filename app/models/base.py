import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, MetaData
from sqlalchemy.dialects.postgresql import BOOLEAN, UUID
from sqlalchemy.orm import declarative_base

metadata_obj = MetaData()
Dcl = declarative_base()


class Base(Dcl):
    __abstract__ = True
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    deleted = Column(BOOLEAN, nullable=True, default=False)

    def __repr__(self):
        return f"{type(self).__name__}[{self.uuid}]"
