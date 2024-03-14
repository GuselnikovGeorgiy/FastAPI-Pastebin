from typing import Optional

from app.database import Base
from sqlalchemy.orm import relationship, mapped_column, Mapped


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    hashed_password: Mapped[str]
    avatar_id: Mapped[Optional[int]] # = 1 как задать дефолт, точнее где

    def __str__(self):
        return f'User {self.email}'
