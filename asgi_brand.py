import asyncio

from app import create_app
from app import settings
from app.services.brand_consumer import BrandConsumer

application = create_app()


async def consumer_brand():
    while True:
        consumer = BrandConsumer(queue=settings.BRANDS_QUEUE, rounting_key=settings.BRANDS_ROUTING_KEY)
        consumer.run()


if __name__ == "__main__":
    asyncio.run(consumer_brand())
