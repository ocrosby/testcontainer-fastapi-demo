"""
CRUD for post
"""

from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.post import Post as PostModel
from app.schemas.post import PostCreate, PostUpdate
from app.core.database import SessionLocal


class CRUDPost:
    """
    CRUD for post
    """

    def __init__(self):
        """
        CRUD for post
        """
        self.db: Session = SessionLocal()

    def create_post(self, post: PostCreate) -> PostModel:
        """
        Create a post

        :param post:
        :return:
        """
        db_post = PostModel(**post.dict())
        self.db.add(db_post)
        self.db.commit()
        self.db.refresh(db_post)
        return db_post

    def get_post(self, post_id: int) -> Optional[PostModel]:
        """
        Get a post

        :param post_id:
        :return:
        """
        return self.db.query(PostModel).filter(PostModel.id == post_id).first()

    def get_posts(self) -> List[PostModel]:
        """
        Get all posts

        :return:
        """
        return self.db.query(PostModel).all()

    def update_post(self, post_id: int, post: PostUpdate) -> Optional[PostModel]:
        """
        Update a post

        :param post_id:
        :param post:
        :return:
        """
        db_post = self.db.query(PostModel).filter(PostModel.id == post_id).first()
        if db_post:
            for key, value in post.dict(exclude_unset=True).items():
                setattr(db_post, key, value)
            self.db.commit()
            self.db.refresh(db_post)
        return db_post

    def delete_post(self, post_id: int) -> bool:
        """
        Delete a post

        :param post_id:
        :return:
        """
        db_post = self.db.query(PostModel).filter(PostModel.id == post_id).first()
        if db_post:
            self.db.delete(db_post)
            self.db.commit()
            return True
        return False


crud_post = CRUDPost()
