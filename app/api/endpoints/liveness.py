"""
This module contains the FastAPI endpoint for the liveness check.
"""

# app/api/endpoints/liveness.py

from fastapi import APIRouter

router = APIRouter()


@router.get("/liveness")
async def liveness():
    """
    This function returns the liveness status of the FastAPI application.

    :return:
    """
    return {"status": "alive"}
