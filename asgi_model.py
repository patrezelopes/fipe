import asyncio

from app import create_app
from app import settings
from app.services.model_consumer import ModelConsumer

application = create_app()


async def consumer_model():
    while True:
        consumer = ModelConsumer(queue=settings.MODELS_QUEUE, rounting_key=settings.MODELS_ROUTING_KEY)
        consumer.run()


if __name__ == "__main__":
    asyncio.run(consumer_model())
