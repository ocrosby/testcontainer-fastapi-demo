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

    class Config:
        """
        This class is used to configure the Pydantic model.
        """
        orm_mode = True
