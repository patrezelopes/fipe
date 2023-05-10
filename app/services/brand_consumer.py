import json
from app.services.tasks import store_brand
from app.services.queue.consumer import Consumer


class BrandConsumer(Consumer):
    def callback_function(self, body):
        super().callback_function(self)
        store_brand.delay(json.loads(body))
