from typing import Optional

from db.connection import get_connection

from app.models.post import Post
from app.exceptions import DatabaseError


def create_table():
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS posts (
                        id SERIAL PRIMARY KEY,
                        title VARCHAR(255) NOT NULL,
                        content TEXT NOT NULL,
                        published BOOLEAN NOT NULL DEFAULT FALSE
                    )
                    """
                )
                conn.commit()
    except Exception as e:
        raise DatabaseError(f"Error creating table: {e}")


def create_post(title: str, content: str, published: bool):
    """
    Create a post

    :param title: the title
    :param content: the content
    :param published: is published
    :return: the post id
    """
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO posts (title, content, published)
                    VALUES (%s, %s, %s)
                    RETURNING id
                    """,
                    (title, content, published),
                )
                post_id = cursor.fetchone()[0]
                conn.commit()

        return post_id
    except Exception as e:
        raise DatabaseError(f"Error creating post: {e}")



def get_all_posts() -> list[Post]:
    """
    Get all posts

    :return: all posts
    """
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, title, content, published FROM posts")
                return [Post(id=id,
                             title=title,
                             content=content,
                             published=published) for id, title, content, published in cursor]
    except Exception as e:
        raise DatabaseError(f"Error getting posts: {e}")


def get_post_by_id(post_id: int) -> Optional[Post]:
    """
    Get post by id

    :param post_id: the post id
    :return: the post
    """
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, title, content, published
                    FROM posts
                    WHERE id = %s
                    """,
                    (post_id,),
                )
                result = cursor.fetchone()
                if result is None:
                    return None

                id, title, content, published = result

        return Post(id=id, title=title, content=content, published=published)
    except Exception as e:
        raise DatabaseError(f"Error getting post: {e}")


def delete_post(post_id: int):
    """
    Delete a post

    :param post_id: the post id
    """
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM posts
                    WHERE id = %s
                    """,
                    (post_id,),
                )
                conn.commit()
                return cursor.rowcount > 0
    except Exception as e:
        raise DatabaseError(f"Error deleting post: {e}")


def update_post(post_id: int, title: str, content: str, published: bool):
    """
    Update a post

    :param post_id: the post id
    :param title: the title
    :param content: the content
    :param published: is published
    """
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE posts
                    SET title = %s, content = %s, published = %s
                    WHERE id = %s
                    """,
                    (title, content, published, post_id),
                )
                conn.commit()
    except Exception as e:
        raise DatabaseError(f"Error updating post: {e}")


def get_post_by_title(title: str) -> Post:
    """
    Get post by title

    :param title: the title
    :return: the post
    """
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, title, content, published
                    FROM posts
                    WHERE title = %s
                    """,
                    (title,),
                )
                id, title, content, published = cursor.fetchone()

        return Post(id=id, title=title, content=content, published=published)
    except Exception as e:
        raise DatabaseError(f"Error getting post: {e}")


def delete_all_posts():
    """
    Delete all posts
    """
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM posts")
                conn.commit()
    except Exception as e:
        raise DatabaseError(f"Error deleting posts: {e}")



