from fastapi import APIRouter

from app.routers.v1 import cars

api_router = APIRouter()
api_router.include_router(cars.router, prefix="/cars", tags=["cars"])