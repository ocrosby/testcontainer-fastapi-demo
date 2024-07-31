"""
This is the main file of the FastAPI application. It creates the FastAPI
app instance and includes the routes from the routes file.
"""

# app/main.py

from fastapi import FastAPI
from app.routes import setup_routes

app = FastAPI()

app.include_router(setup_routes())
