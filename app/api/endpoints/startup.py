"""
This module contains the FastAPI application startup endpoint.
"""

# app/api/endpoints/startup.py

from fastapi import APIRouter

router = APIRouter()


@router.get("/startup")
async def startup():
    """
    This function returns the startup status of the FastAPI application.

    :return:
    """
    return {"status": "started"}
