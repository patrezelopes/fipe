from fastapi import APIRouter

from app.routers.v1.views.parallelum import router as parallelum

api_router = APIRouter()
api_router.include_router(parallelum, prefix="/fipe", tags=["fipe"])