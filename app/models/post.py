"""
Post model
"""

from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Post(Base):
    """
    Post model
    """

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, index=True)
    title = Column(String, index=True)
    body = Column(String, index=True)
