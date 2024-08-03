"""
Post endpoints
"""

from typing import List

from fastapi import APIRouter, HTTPException

from app.crud.post import CRUDPost
from app.models.post import Post

router = APIRouter()


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
    return CRUDPost().create_post(post)


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
    post = CRUDPost().get_post(post_id)
    if post is None:
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
    return CRUDPost().get_posts()


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
    updated_post = CRUDPost().update_post(post_id, post)
    if updated_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post


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
    success = CRUDPost().delete_post(post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return success
