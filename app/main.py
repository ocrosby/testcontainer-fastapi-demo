"""
This is the main file of the FastAPI application. It creates the FastAPI
app instance and includes the routes from the routes file.
"""

# app/main.py

from fastapi import FastAPI
from app.routes import setup_routes
from app.core.database import engine, Base

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

app.include_router(setup_routes())
