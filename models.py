from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from .basemodel import BaseClass
from .crypt import verify_password


class User(BaseClass):
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(15), nullable=False, unique=True)
    verify: Mapped[bool] = mapped_column(Boolean(), default=False)
    password: Mapped[str] = mapped_column(String(256), nullable=False)

    def __str__(self) -> str:
        return f"{self.username}, {self.phone}, {self.email}"

    def check_password(self, decrypted_password: str) -> bool:
        return verify_password(decrypted_password, self.password)
