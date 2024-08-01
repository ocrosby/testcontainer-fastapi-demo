"""
This is the main file of the FastAPI application. It creates the FastAPI
app instance and includes the routes from the routes file.
"""

# app/main.py

from dotenv import load_dotenv
from fastapi import FastAPI
from app.routes import setup_routes

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

app.include_router(setup_routes())

# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run(app, host="0.0.0.0")
