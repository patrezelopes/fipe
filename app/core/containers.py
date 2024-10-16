from dependency_injector import containers, providers

from app.repository.dependencies import get_db
from app.repository.nosql_repository import NoSqlRepository
from app.repository.sql_repository import SqlRepository
from app.use_cases.car import CarUseCase


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(packages=["app.routers.v1.cars"])

    db_session = providers.Resource(
        get_db
    )

    car_repository = providers.Factory(
        SqlRepository,
        db_session
    )

    car_repository_no_sql = providers.Factory(
        NoSqlRepository,
        db_session
    )

    car_use_case = providers.Factory(
        CarUseCase,
        repository=car_repository
    )

    car_use_case_no_sql = providers.Factory(
        CarUseCase,
        repository=car_repository_no_sql
    )


    # Business rules