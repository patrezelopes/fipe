from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.containers import Container
from app.use_cases.car import CarUseCaseInterface

router = APIRouter()

@router.get("/")
@inject
def list(car_use_case: CarUseCaseInterface = Depends(Provide[Container.car_use_case])):
    cars = car_use_case.list()
    return cars

@router.get("/cached_list")
@inject
def list(car_use_case: CarUseCaseInterface = Depends(Provide[Container.car_use_case_no_sql])):
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