from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr
from typing_extensions import Annotated


class SUserRegister(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(30)]
    email: EmailStr
    password: str


class SUserLogin(BaseModel):
    email: EmailStr
    password: str
