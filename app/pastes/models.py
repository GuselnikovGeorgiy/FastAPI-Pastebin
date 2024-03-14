from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, Date, String
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Pastes(Base):
    __tablename__ = "pastes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    body: Mapped[str]
    is_private: Mapped[bool]
    hashed_password: Mapped[Optional[str]]
    expire_date: Mapped[datetime] = mapped_column(Date)
    num_views: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))


