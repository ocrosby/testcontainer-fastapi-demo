"""
Post endpoints
"""

from typing import List

from fastapi import APIRouter, HTTPException

from app.models.post import Post
from app.crud.post import crud_post

router = APIRouter()


@router.post("/", response_model=Post)
async def create_post(post: Post):
    """
    Create a post

    :param post:
    :return:
    """
    return crud_post.create_post(post)


@router.get("/{post_id}", response_model=Post)
async def read_post(post_id: int):
    """
    Get a post

    :param post_id:
    :return:
    """
    post = crud_post.get_post(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.get("/", response_model=List[Post])
async def read_posts():
    """
    Get all posts

    :return:
    """
    return crud_post.get_posts()


@router.put("/{post_id}", response_model=Post)
async def update_post(post_id: int, post: Post):
    """
    Update a post

    :param post_id:
    :param post:
    :return:
    """
    updated_post = crud_post.update_post(post_id, post)
    if updated_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post


@router.delete("/{post_id}", response_model=bool)
async def delete_post(post_id: int):
    """
    Delete a post

    :param post_id:
    :return:
    """
    success = crud_post.delete_post(post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return success
