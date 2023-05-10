import json
from app.services.tasks import store_model
from app.services.queue.consumer import Consumer


class ModelConsumer(Consumer):
    def callback_function(self, body):
        super().callback_function(self)
        store_model.delay(json.loads(body))
