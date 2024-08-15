from typing import Optional

from db.connection import get_connection

from app.models.post import Post


def create_table():
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


def create_post(title: str, content: str, published: bool):
    """
    Create a post

    :param title: the title
    :param content: the content
    :param published: is published
    :return: the post id
    """
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


def get_all_posts() -> list[Post]:
    """
    Get all posts

    :return: all posts
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, title, content, published FROM posts")
            return [Post(id=id,
                         title=title,
                         content=content,
                         published=published) for id, title, content, published in cursor]


def get_post_by_id(post_id: int) -> Optional[Post]:
    """
    Get post by id

    :param post_id: the post id
    :return: the post
    """
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


def delete_post(post_id: int):
    """
    Delete a post

    :param post_id: the post id
    """
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


def update_post(post_id: int, title: str, content: str, published: bool):
    """
    Update a post

    :param post_id: the post id
    :param title: the title
    :param content: the content
    :param published: is published
    """
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


def get_post_by_title(title: str) -> Post:
    """
    Get post by title

    :param title: the title
    :return: the post
    """
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


def delete_all_posts():
    """
    Delete all posts
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM posts")
            conn.commit()



