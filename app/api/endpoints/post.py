"""
Post endpoints
"""
from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.models.post import Post
from app.schemas.post import PostCreate, PostResponse
from app.db.connection import get_db

router = APIRouter()


@router.post(
    path="/",
    response_model=PostCreate,
    tags=["posts"]
)
async def create_post(post: PostCreate, db: Session = Depends(get_db)):
    """
    Create a post

    :param post: the post
    :param db: the database session
    :return:
    """
    try:
        # Create a new post instance
        db_post = Post(title=post.title, content=post.content, published=post.published)

        # Add the post to the database
        db.add(db_post)
        db.commit()
        db.refresh(db_post)

        return db_post
    except SQLAlchemyError as e:
        # Rollback the transaction
        db.rollback()

        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


# Get a specific post by ID
@router.get(path="/posts/{post_id}", response_model=PostResponse, tags=["posts"])
def read_post(post_id: int, db: Session = Depends(get_db)):
    try:
        post = db.query(Post).filter(Post.id == post_id).first()
        if post is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
        return post
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


# Get all posts
@router.get(path="/", response_model=List[PostResponse], tags=["posts"])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get all posts

    :param skip: the number of posts to skip
    :param limit: the number of posts to return
    :param db: the database session
    :return: the list of posts
    """
    try:
        posts = db.query(Post).offset(skip).limit(limit).all()
        return posts
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


# Update a post
@router.put("/posts/{post_id}", response_model=PostResponse, tags=["posts"])
def update_post(post_id: int, post: PostCreate, db: Session = Depends(get_db)):
    """
    Update a post

    :param post_id: the post ID
    :param post: the post
    :param db: the database session
    :return: the updated post
    """
    try:
        db_post = db.query(Post).filter(Post.id == post_id).first()
        if db_post is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

        for key, value in post.dict().items():
            setattr(db_post, key, value)

        db.commit()
        db.refresh(db_post)

        return db_post
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


# Delete a post
@router.delete("/posts/{post_id}", response_model=PostResponse, tags=["posts"])
def delete_post(post_id: int, db: Session = Depends(get_db)):
    """
    Delete a post

    :param post_id: the post ID
    :param db: the database session
    :return: the deleted post
    """
    try:
        db_post = db.query(Post).filter(Post.id == post_id).first()
        if db_post is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

        db.delete(db_post)
        db.commit()

        return db_post
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
