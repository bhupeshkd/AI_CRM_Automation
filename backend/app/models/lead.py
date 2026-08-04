from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Lead(Base):
    __tablename__ = "leads"

    # ==========================
    # Primary Key
    # ==========================
    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )

    # ==========================
    # Customer Information
    # ==========================
    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
        index=True
    )

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    # ==========================
    # Lead Information
    # ==========================
    vehicle_interest: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    budget: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    purchase_timeline: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    lead_source: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="Website"
    )

    # ==========================
    # AI Qualification
    # ==========================
    lead_score: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    qualification_status: Mapped[str] = mapped_column(
        String(20),
        default="Pending"
    )

    pipeline_stage: Mapped[str] = mapped_column(
        String(30),
        default="New Lead"
    )

    # ==========================
    # Audit Fields
    # ==========================
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )