import uuid

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr
from typing_extensions import Annotated


class SNewPaste(BaseModel):
    title: Annotated[str, MaxLen(200)]
    body: str


class SUpdatePaste(BaseModel):
    title: Annotated[str, MaxLen(200)]
    body: str
