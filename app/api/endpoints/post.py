"""
Post endpoints
"""
import app.dal.posts as posts_dal

from typing import List

from fastapi import APIRouter, HTTPException

from app.models.post import Post
from app.config.logging import logger

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
async def create_post(post: Post):
    """
    Create a post

    :param post:
    :return:
    """
    return posts_dal.create_post(post.title, post.content, post.published)


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
    post = posts_dal.get_post_by_id(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return post


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
    return posts_dal.get_all_posts()


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
    posts_dal.update_post(post_id, post.title, post.content, post.published)

    return posts_dal.get_post_by_id(post_id)


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
    return posts_dal.delete_post(post_id)


