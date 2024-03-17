import datetime
import uuid
from typing import Optional, Annotated


from sqlalchemy import ForeignKey, Date, String, text, func
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.users.models import Users


uuid_pk = Annotated[uuid.UUID, mapped_column(primary_key=True, default=str(uuid.uuid4()))]

created_at = Annotated[
    datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))
]
updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow,
    ),
]


class Pastes(Base):
    __tablename__ = "pastes"

    id: Mapped[uuid_pk]
    title: Mapped[str] = mapped_column(String(200))
    body: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    users: Mapped["Users"] = relationship(back_populates="pastes")

    def __str__(self):
        return f"Paste: {self.title}"
