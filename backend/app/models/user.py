from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    # ==========================
    # Primary Key
    # ==========================

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )

    # ==========================
    # Basic Information
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

    # ==========================
    # Authentication
    # ==========================

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    # ==========================
    # Authorization
    # ==========================

    role: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="Sales Executive"
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True
    )

    # ==========================
    # Audit Fields
    # ==========================

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )