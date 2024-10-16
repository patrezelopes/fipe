from dependency_injector.wiring import Provide
from fastapi import APIRouter, Depends

from app.core.containers import Container
from app.use_cases.car import CarUseCaseInterface

router = APIRouter()

@router.get("/")
def list(car_use_case: CarUseCaseInterface = Depends(Provide[Container.car_use_case])):
    cars = car_use_case.list()
    return cars

@router.post("/create")
def create():
    pass

@router.put("/edit/{id}")
def update():
    pass

@router.delete("/delete/{id}")
def delete():
    pass