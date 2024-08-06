"""
This is the main file of the FastAPI application. It creates the FastAPI
app instance and includes the routes from the routes file.
"""

# app/main.py

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import setup_routes
from app.config.logging import logger
from app.core.config import settings

# Load environment variables from .env file
load_dotenv()

api = FastAPI(
    title="FastAPI Demo",
    description=settings.description,
    summary=settings.summary,
    version=settings.version,
    contact=settings.contact,
    license_info=settings.license_info,
    openapi_tags=settings.tag_metadata,
)

# Add CORS middleware if needed
api.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if not hasattr(api, 'dependency_overrides'):
    api.dependency_overrides = {}


# Middleware to log requests
@api.middleware("http")
async def log_requests(request, call_next):
    """
    Middleware to log requests

    :param request:
    :param call_next:
    :return:
    """
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response Status: {response.status_code}")
    return response

api.include_router(router=setup_routes())

