"""
This module contains the Country model.
"""

from sqlalchemy import String, Integer, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base


class Country(Base):
    """
    Country model
    """
    __tablename__ = "countries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    code: Mapped[str] = mapped_column(String(10))

    __table_args__ = (
        UniqueConstraint("name", name="unique_country_name"),
        UniqueConstraint("code", name="unique_country_code"),
        Index("idx_country_name", "name"),
        Index("idx_country_code", "code"),
    )

    def __repr__(self):
        """
        Return a string representation of the Country model

        :return:
        """
        return f"Country(id={self.id!r}, name={self.name!r}, code={self.code!r})"
