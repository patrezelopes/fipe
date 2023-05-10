import json
import logging

from fastapi import APIRouter, Request
from starlette.responses import JSONResponse

from app.exceptions import HTTPError
from app.repository.brand import BrandCollectionRepository
from app.schemas.model import ModelRequestToCreateSchema
from app.services.tasks import get_brands, get_models

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/")
def brands():
    try:
        get_brands.delay()
    except Exception:
        raise HTTPError(status_code=502, detail="unexpected error")
    else:
        return JSONResponse(content={"response": "First load brands"})


@router.post("/model")
def models(model: ModelRequestToCreateSchema):
    try:
        get_models.delay(brand=model.brand)
    except Exception:
        raise HTTPError(status_code=502, detail="unexpected error")
    else:
        return JSONResponse(content={"response": "Loading brands"}, status_code=202)


@router.get("/brands")
def brands():
    try:
        brands = BrandCollectionRepository.find()
    except Exception:
        raise HTTPError(status_code=502, detail="unexpected error")
    else:
        return brands


@router.get("/brands/{brand_id}")
def brands(brand_id: int):
    try:
        brand = BrandCollectionRepository.find_one(brand=brand_id)
    except Exception:
        raise HTTPError(status_code=502, detail="unexpected error")
    else:
        return brand


@router.get("/models")
def models():
    try:
        brands = BrandCollectionRepository.find()
    except Exception:
        raise HTTPError(status_code=502, detail="unexpected error")
    else:
        return brands


@router.get("/models/{model_id}")
def brands(model_id: int):
    try:
        brand = BrandCollectionRepository.find(model=model_id)
    except Exception:
        raise HTTPError(status_code=502, detail="unexpected error")
    else:
        return brand
