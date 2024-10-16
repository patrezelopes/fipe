from abc import ABC

from app.repository.base import AbstractRepository


class CarUseCaseInterface(ABC):
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def list(self):
        pass

    def get_by_id(self, id: int):
        pass

    def create(self, data):
        pass

    def update(self, id: int, data):
        pass

    def remove(self, id: int):
        pass