from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column


from app.database.database import Base


class FollowUp(Base):

    __tablename__ = "follow_ups"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )

    lead_id: Mapped[str] = mapped_column(
        ForeignKey("leads.id"),
        nullable=False
    )

    follow_up_type: Mapped[str] = mapped_column(
        String(30),
        default="Call"
    )

    scheduled_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="Pending"
    )

    remarks: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )