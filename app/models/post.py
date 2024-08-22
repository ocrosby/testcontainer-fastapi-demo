"""
This module contains the Post model.
"""

from typing import Optional
from sqlalchemy import String, Integer, Boolean, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base
from pydantic import BaseModel

class Post(BaseModel):
    id: int
    name: str
    content: Optional[str]
    published: bool


class DBPost(Base):
    """
    Post model
    """
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    published: Mapped[bool] = mapped_column(Boolean, default=False)

    __table_args__ = (
        UniqueConstraint("title", name="unique_post_title"),
        Index("idx_post_title", "title"),
    )

    def __repr__(self):
        """
        Return a string representation of the Post model

        :return:
        """
        return f"Post(id={self.id!r}, title={self.title!r}, content={self.content!r}, published={self.published!r})"
