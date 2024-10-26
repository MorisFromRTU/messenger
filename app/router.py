from app.routers import users_router
from fastapi import FastAPI

def setup_routes(app: FastAPI):
    app.include_router(users_router, prefix="/users")