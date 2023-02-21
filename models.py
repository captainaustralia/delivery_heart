from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from basemodel import BaseClass


class User(BaseClass):
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(15), nullable=False, unique=True)
    verify: Mapped[bool] = mapped_column(Boolean(), default=False)

    def __str__(self) -> str:
        return f"{self.username}, {self.phone}, {self.email}"
