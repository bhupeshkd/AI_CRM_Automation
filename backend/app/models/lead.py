
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
    nullable=False,
    default=0
    )

    qualification_status: Mapped[str] = mapped_column(
    String(20),
    nullable=False,
    default="Pending"
    )

    pipeline_stage: Mapped[str] = mapped_column(
    String(30),
    nullable=False,
    default="New Lead"
    )

    priority: Mapped[str] = mapped_column(
    String(20),
    nullable=False,
    default="Medium"
    )

    recommended_action: Mapped[str] = mapped_column(
        String(500),
        nullable=True
    )
  
    follow_up_in_hours: Mapped[int] = mapped_column(
    Integer,
    nullable=False,
    default=24
    )

    ai_reason: Mapped[str] = mapped_column(
        String(1000),
        nullable=True
    )

    # ==========================
    # CRM Fields
    # ==========================

    notes: Mapped[str] = mapped_column(
        String(1000),
        nullable=True
    )

    tags: Mapped[str] = mapped_column(
        String(500),
        nullable=True
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

    # ==========================
    # AI Appointment Recommendation
    # ==========================

    suggested_appointment_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    suggested_meeting_type: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
        default="Test Drive"
    )

    appointment_recommendation_status: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
        default="Awaiting Confirmation"
    )
        