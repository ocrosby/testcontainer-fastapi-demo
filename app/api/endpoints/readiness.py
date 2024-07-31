"""
This module contains the FastAPI application readiness endpoint.
"""

# app/api/endpoints/readiness.py

from fastapi import APIRouter

router = APIRouter()


@router.get("/readiness")
async def readiness():
    """
    This function returns the readiness status of the FastAPI application.

    :return:
    """
    return {"status": "ready"}
