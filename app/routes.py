"""
This module sets up the routes for the FastAPI application.
"""

# app/routes.py

from fastapi import APIRouter
from app.api.endpoints import readiness, liveness, startup
from app.api.endpoints import post


def setup_routes() -> APIRouter:
    """
    This function sets up the routes for the FastAPI application.
    :return: APIRouter
    """

    router = APIRouter()
    router.include_router(readiness.router, prefix="/health")
    router.include_router(liveness.router, prefix="/health")
    router.include_router(startup.router, prefix="/health")
    router.include_router(post.router, prefix="/posts")

    return router
