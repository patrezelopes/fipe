from app.use_cases.car_interface import CarUseCaseInterface


class CarUseCase(CarUseCaseInterface):
    def list(self, query):
        return self.repository.list(query=query)

    def get_by_id(self, id: int):
        return self.repository.get(id=id)

    def create(self, data):
        return self.repository.create(data)

    def update(self, id: int, data):
        return self.repository.update(id=id, data=data)

    def remove(self, id: int):
        return self.repository.delete(id=id)
