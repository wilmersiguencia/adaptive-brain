from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    # ==========================
    # Identificación
    # ==========================
    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    # ==========================
    # Información personal
    # ==========================
    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    birth_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    profile_image: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    # ==========================
    # Acceso
    # ==========================
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    # ==========================
    # Configuración
    # ==========================
    language: Mapped[str] = mapped_column(
        String(10),
        default="es"
    )

    timezone: Mapped[str] = mapped_column(
        String(50),
        default="America/Guayaquil"
    )

    # ==========================
    # Estado
    # ==========================
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    # ==========================
    # Auditoría
    # ==========================
    last_login: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )