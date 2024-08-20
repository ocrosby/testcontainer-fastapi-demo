"""
This is the main file of the FastAPI application. It creates the FastAPI
app instance and includes the routes from the routes file.
"""

# app/main.py
import os

from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import setup_routes
from app.core.config import settings
from app.core.logging import logger

# Load environment variables from .env file
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager

    :param app:
    :return:
    """
    try:
        logger.info(f"Application starting up http://{settings.host}:{settings.port}/docs")
        yield
    finally:
        logger.info("Application shutting down")

api = FastAPI(
    title="FastAPI Demo",
    description=settings.description,
    summary=settings.summary,
    version=settings.version,
    contact=settings.contact,
    license_info=settings.license_info,
    openapi_tags=settings.tag_metadata,
    lifespan=lifespan,
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

if __name__ == "__main__":
    import uvicorn

    app_string = "app.main:api"
    host_string = "0.0.0.0"
    port_string = os.environ.get("PORT", 80)
    port = int(port_string)

    logger.info(f"Starting server on {host_string}:{port}")

    uvicorn.run(app=app_string, host=host_string, port=port)
