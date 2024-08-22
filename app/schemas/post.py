"""
Post schemas
"""

from pydantic import BaseModel


class PostBase(BaseModel):
    """
    Post base
    """
    title: str
    content: str
    published: bool


class PostCreate(PostBase):
    """
    Post create
    """


class PostUpdate(PostBase):
    """
    Post update
    """


class PostResponse(PostBase):
    id: int

    class Config:
        from_attributes = True
