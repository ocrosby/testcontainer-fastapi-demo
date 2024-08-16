"""
This module contains the State model.
"""

from sqlalchemy import String, Integer, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base


class State(Base):
    """
    State model
    """
    __tablename__ = "states"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    abbreviation: Mapped[str] = mapped_column(String(10))
    country_id: Mapped[int] = mapped_column(Integer, ForeignKey("countries.id"))

    __table_args__ = (
        UniqueConstraint("name", name="unique_state_name"),
        UniqueConstraint("abbreviation", name="unique_state_abbreviation"),
        Index("idx_state_name", "name"),
        Index("idx_state_abbreviation", "abbreviation"),
    )

    def __repr__(self):
        """
        Return a string representation of the State model

        :return:
        """
        return f"State(id={self.id!r}, name={self.name!r}, abbreviation={self.abbreviation!r})"
