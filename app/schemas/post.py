"""
Post schemas
"""
from typing import Optional

from pydantic import BaseModel


class PostBase(BaseModel):
    """
    Post base
    """
    title: str
    content: str
    published: bool


class PostCreate(BaseModel):
    """
    Post create
    """
    title: str
    content: Optional[str]
    published: Optional[bool]


class PostUpdate(BaseModel):
    """
    Post update
    """
    title: Optional[str]
    content: Optional[str]
    published: Optional[bool]


class PostResponse(PostBase):
    id: int

    class Config:
        from_attributes = True
