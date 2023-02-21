import uuid
from uuid import UUID as ID

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime


class BaseClass(DeclarativeBase):
    __abstract__ = True
    __tablename__ = None

    uid: Mapped[ID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())

    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

