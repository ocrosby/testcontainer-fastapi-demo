"""
This module contains the FastAPI application startup endpoint.
"""

# app/api/endpoints/startup.py

from fastapi import APIRouter, HTTPException
from app.core.database import check_database_connection

router = APIRouter()


@router.get("/startup")
async def startup():
    """
    This function returns the startup status of the FastAPI application.

    :return:
    """
    if not check_database_connection():
        raise HTTPException(status_code=503, detail="Service Unavailable")

    return {"status": "started"}
