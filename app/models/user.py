"""
This module contains the User model.
"""

from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, DateTime, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base
from app.models.address import Address


class User(Base):
    """
    User model
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(100))
    full_name: Mapped[Optional[str]] = mapped_column(String(100))
    addresses: Mapped[List["Address"]] = relationship(back_populates="user", cascade="all, delete, delete-orphan")
    is_active: Mapped[bool] = mapped_column(default=True)
    hashed_password: Mapped[str] = mapped_column(String(100))
    last_login: Mapped[datetime] = mapped_column(DateTime)
    last_login_ip: Mapped[str] = mapped_column(String(45))

    __table_args__ = (
        UniqueConstraint("email", name="unique_user_email"),
        UniqueConstraint("name", name="unique_user_name"),
        Index("idx_user_name", "name"),
        Index("idx_user_email", "email"),
    )

    def __repr__(self):
        """
        Return a string representation of the User model

        :return:
        """
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.full_name!r})"
