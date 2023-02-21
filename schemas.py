from pydantic import BaseModel
from pydantic.types import UUID as ID


class UserWriteSchema(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    phone: str


class UserReadSchema(BaseModel):
    uid: ID
    username: str
    first_name: str
    last_name: str
    email: str
    phone: str
