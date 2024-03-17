from typing import Optional, Annotated
from uuid import UUID

from app.database import Base
from sqlalchemy.orm import relationship, mapped_column, Mapped


uuid_pk = Annotated[UUID, mapped_column(primary_key=True)]


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[uuid_pk]
    username: Mapped[str]
    email: Mapped[str]
    hashed_password: Mapped[str]
    avatar_id: Mapped[Optional[int]] # = 1 как задать дефолт, точнее где

    def __str__(self):
        return f'User {self.email}'
