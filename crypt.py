import contextlib

import passlib.exc
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    :param plain_password:  Default password form.
    :param hashed_password: Password in hash form.
    :return: equal hash == plain
    """
    with contextlib.suppress(passlib.exc.UnknownHashError):
        return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    :param password:  Default password form.
    :return: hashed password
    """
    return pwd_context.hash(password)
