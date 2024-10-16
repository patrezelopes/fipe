from app.repository.base import AbstractRepository


class SqlRepository(AbstractRepository):
    def list(self, query=None):
        return ['car1', 'car2', 'car3']
        #pass

    def get(self, id):
        pass

    def create(self, data):
        pass

    def update(self, id, data):
        pass

    def delete(self, id):
        pass