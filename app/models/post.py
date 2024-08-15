"""
This module contains the Post model.
"""

from typing import Optional
from pydantic import BaseModel


class Post(BaseModel):
    """
    Post model
    """
    id: Optional[int]
    title: str
    content: str
    published: bool

    class Config:
        """
        This class is used to configure the Pydantic model.
        """
        from_attributes = True

    def __str__(self):
        return f"Post(id={self.id}, title={self.title}, content={self.content})"
