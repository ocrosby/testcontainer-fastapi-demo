"""
Post schemas
"""

from pydantic import BaseModel


class PostBase(BaseModel):
    """
    Post base
    """
    userId: int
    title: str
    body: str


class PostCreate(PostBase):
    """
    Post create
    """


class PostUpdate(PostBase):
    """
    Post update
    """


class Post(PostBase):
    """
    Post model
    """
    id: int

    class Config:
        """
        Config
        """
        from_attributes = True
