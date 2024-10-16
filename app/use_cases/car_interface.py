from abc import ABC

from app.repository.base import AbstractRepository


class CarUseCaseInterface(ABC):
    def __init__(self, repository: AbstractRepository):
        self.repository = repository
