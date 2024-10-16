from app.repository.base import AbstractRepository


class NoSqlRepository(AbstractRepository):
    def list(self, query=None):
        return ['cached_car1', 'cached_car2', 'cached_car3']

    def get(self, id):
        pass

    def create(self, data):
        pass

    def update(self, id, data):
        pass

    def delete(self, id):
        pass