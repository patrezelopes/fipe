import logging
from app import settings
from app.repository.brand import BrandCollectionRepository
from app.repository.model import ModelCollectionRepository
from app.schemas.brand import BrandCreateSchema
from app.schemas.model import ModelCreateSchema
from app.services.fipe.proxy import Fipe
from app.services.parallelum.proxy import Parallelum
from app.services.queue.producer import Producer
from app.services.worker import app

logger = logging.getLogger(__name__)


@app.task(name='get_brands', bind=True)
def get_brands(_):
    brands = Parallelum().get_brands()
    producer = Producer(exchange="brands")
    for brand in brands:
        try:
            producer.publish(settings.BRANDS_ROUTING_KEY, brand)
        except Exception as e:
            message = {"exception": e}
            logger.error(message)


@app.task(name='get_model', bind=True)
def get_models(_, brand):
    models = Parallelum().get_models_info(brand)
    producer = Producer(exchange="models")
    for model in models.get("modelos"):
        model["brand"] = brand
        try:
            producer.publish(settings.MODELS_ROUTING_KEY, model)
        except Exception as e:
            message = {"exception": e}
            logger.error(message)


@app.task(name='store_brand', bind=True)
def store_brand(_, brand):
    brand_schema = BrandCreateSchema(code=brand.get("codigo"), name=brand.get("nome"))
    BrandCollectionRepository.insert(brand_schema)
    # fipe_service = Fipe()
    # fipe_service.set_model_info(brand_schema.code)


@app.task(name='store_model', bind=True)
def store_model(_, model):
    model_schema = ModelCreateSchema(brand=model.get("brand"), code=model.get("codigo"), name=model.get("nome"))
    ModelCollectionRepository.insert(model_schema)


@app.task(name='check', bind=True, time_limit=20)
def check(_):
    output = 'cache ok'
    return dict(output=output)
