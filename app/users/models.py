import uuid
from typing import Optional, Annotated

from sqlalchemy import func

from app.database import Base
from sqlalchemy.orm import relationship, mapped_column, Mapped


uuid_pk = Annotated[
    uuid.UUID, mapped_column(primary_key=True, default=func.gen_random_uuid())
]


class Users(Base):
    __tablename__ = "users"

    id: Mapped[uuid_pk]
    username: Mapped[str]
    email: Mapped[str]
    hashed_password: Mapped[str]

    def __str__(self):
        return f"User {self.email}"
