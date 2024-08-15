"""
Post endpoints
"""
import app.dal.posts as posts_dal

from typing import List

from fastapi import Request, APIRouter, HTTPException

from app.models.post import Post
from core.logging import logger

router = APIRouter()


def init():
    """
    Initialize the posts table

    :return:
    """
    logger.info("Initializing the posts table ...")
    posts_dal.create_table()


init()


@router.post(
    path="/",
    response_model=Post,
    tags=["posts"]
)
async def create_post(request: Request, post: Post):
    """
    Create a post

    :param request: the request
    :param post: the post
    :return:
    """
    try:
        if not isinstance(post, Post):
            raise HTTPException(status_code=400, detail="Invalid post")

        return posts_dal.create_post(post.title, post.content, post.published)
    except HTTPException as e:
        logger.error(f"Error creating post: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error creating post: {e}")
        raise HTTPException(status_code=500, detail="Error creating post")


@router.get(
    path="/{post_id}",
    response_model=Post,
    tags=["posts"]
)
async def read_post(post_id: int):
    """
    Get a post

    :param post_id:
    :return:
    """
    # If the post does not exist, raise an HTTPException
    try:
        post = posts_dal.get_post_by_id(post_id)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        return post
    except Exception as e:
        logger.error(f"Error getting post: {e}")
        raise HTTPException(status_code=500, detail="Error getting post")


@router.get(
    path="/",
    response_model=List[Post],
    tags=["posts"]
)
async def read_posts():
    """
    Get all posts

    :return:
    """
    try:
        return posts_dal.get_all_posts()
    except Exception as e:
        logger.error(f"Error getting posts: {e}")
        raise HTTPException(status_code=500, detail="Error getting posts")


@router.put(
    path="/{post_id}",
    response_model=Post,
    tags=["posts"]
)
async def update_post(post_id: int, post: Post):
    """
    Update a post

    :param post_id:
    :param post:
    :return:
    """
    try:
        posts_dal.update_post(post_id, post.title, post.content, post.published)

        return posts_dal.get_post_by_id(post_id)
    except Exception as e:
        logger.error(f"Error updating post: {e}")
        raise HTTPException(status_code=500, detail="Error updating post")


@router.delete(
    path="/{post_id}",
    response_model=bool,
    tags=["posts"]
)
async def delete_post(post_id: int):
    """
    Delete a post

    :param post_id:
    :return:
    """
    try:
        return posts_dal.delete_post(post_id)
    except Exception as e:
        logger.error(f"Error deleting post: {e}")
        raise HTTPException(status_code=500, detail="Error deleting post")


