from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, Text, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Conversation(Base):

    __tablename__ = "conversations"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )

    lead_id: Mapped[str] = mapped_column(
        ForeignKey("leads.id"),
        nullable=False
    )

    sender: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    message: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    message_type: Mapped[str] = mapped_column(
    String(30),
    nullable=False,
    default="Note"
    )

    created_at: Mapped[datetime] = mapped_column(
    DateTime,
    nullable=False,
    default=datetime.utcnow
    )