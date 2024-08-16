"""
This module contains the City model.
"""

from sqlalchemy import String, Integer, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base


class City(Base):
    """
    City model
    """
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    state_id: Mapped[int] = mapped_column(Integer, ForeignKey("states.id"))

    __table_args__ = (
        UniqueConstraint("name", name="unique_city_name"),
        Index("idx_city_name", "name"),
    )

    def __repr__(self):
        """
        Return a string representation of the City model

        :return:
        """
        return f"City(id={self.id!r}, name={self.name!r})"
