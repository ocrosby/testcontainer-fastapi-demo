"""
This module contains the Address model.
"""

from sqlalchemy import Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base


class Address(Base):
    """
    Address model
    """
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str] = mapped_column(String(100))
    city: Mapped[str] = mapped_column(String(50))
    state_id: Mapped[int] = mapped_column(Integer, ForeignKey("states.id"))
    zip_code: Mapped[str] = mapped_column(String(20))
    country_id: Mapped[int] = mapped_column(Integer, ForeignKey("countries.id"))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    __table_args__ = (
        UniqueConstraint("street", "city", "state_id", "zip_code", name="unique_address"),
        Index("idx_address_street", "street"),
        Index("idx_address_city", "city"),
        Index("idx_address_zip_code", "zip_code"),
    )

    def __repr__(self):
        """
        Return a string representation of the Address model

        :return:
        """
        return f"Address(id={self.id!r}, street={self.street!r}, city={self.city!r}, state={self.state!r}, zip_code={self.zip_code!r})"
