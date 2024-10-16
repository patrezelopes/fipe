from abc import abstractmethod, ABC
from typing import Optional


class AbstractRepository(ABC):

    def __init__(self, session):
        self.session=session
    @abstractmethod
    def list(self, query: Optional[dict] = None) -> list[dict]:
        pass

    @abstractmethod
    def get(self, id: int) -> dict:
        pass

    @abstractmethod
    def create(self, data: dict) -> dict:
        pass

    @abstractmethod
    def update(self, id: int, data: dict) -> dict:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass