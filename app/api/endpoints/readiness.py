"""
This module contains the FastAPI application readiness endpoint.
"""

# app/api/endpoints/readiness.py

from fastapi import APIRouter, HTTPException
from app.core.database import check_database_connection


router = APIRouter()


@router.get("/readiness")
async def readiness():
    """
    This function returns the readiness status of the FastAPI application.

    :return:
    """
    if not check_database_connection():
        raise HTTPException(status_code=503, detail="Service Unavailable")

    return {"status": "ready"}
