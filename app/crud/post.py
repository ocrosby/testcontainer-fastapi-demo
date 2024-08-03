"""
CRUD for post
"""

from typing import List, Optional

from app.schemas.post import PostCreate, PostUpdate
from app.core.database import get_db_connection


class CRUDPost:
    """
    CRUD for post
    """

    def __init__(self):
        """
        CRUD for post
        """
        self.conn = get_db_connection()

    def create_post(self, post: PostCreate) -> int:
        """
        Create a post

        :param post:
        :return: post_id
        """
        with self.conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO posts (title, content, published)
                VALUES (%s, %s, %s)
                RETURNING id
                """,
                (post.title, post.content, post.published),
            )
            post_id = cursor.fetchone()[0]
            self.conn.commit()

        return post_id

    def get_post(self, post_id: int) -> Optional[dict]:
        """
        Get a post

        :param post_id:
        :return: post data as dictionary
        """
        with self.conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, title, content, published
                FROM posts
                WHERE id = %s
                """,
                (post_id,),
            )
            post = cursor.fetchone()

        return dict(post) if post else None

    def get_posts(self) -> List[dict]:
        """
        Get all posts

        :return: list of post data as dictionaries
        """
        with self.conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, title, content, published
                FROM posts
                """
            )
            posts = cursor.fetchall()

        return [dict(post) for post in posts]

    def update_post(self, post_id: int, post: PostUpdate) -> bool:
        """
        Update a post

        :param post_id:
        :param post:
        :return: True if post is updated, False otherwise
        """
        with self.conn.cursor() as cursor:
            cursor.execute(
                """
                UPDATE posts
                SET title = %s, content = %s, published = %s
                WHERE id = %s
                """,
                (post.title, post.content, post.published, post_id),
            )
            self.conn.commit()

        return cursor.rowcount > 0

    def delete_post(self, post_id: int) -> bool:
        """
        Delete a post

        :param post_id:
        :return: True if post is deleted, False otherwise
        """
        with self.conn.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM posts
                WHERE id = %s
                """,
                (post_id,),
            )
            self.conn.commit()

        return cursor.rowcount > 0


# crud_post = CRUDPost()
