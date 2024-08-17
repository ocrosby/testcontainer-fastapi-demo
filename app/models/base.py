"""
This module contains the base class for all models.
"""

from datetime import datetime, UTC
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    """
    Base class for all models
    """
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(UTC), onupdate=datetime.now(UTC))
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
