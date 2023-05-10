from celery import Celery
from celery.schedules import crontab
from app.config import settings

app = Celery(broker=f"{settings.BROKER_URL}", backend=None)

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-health-check': {
        'task': 'check',
        'schedule': crontab(minute='*/1'),
    },
}
app.conf.timezone = 'UTC'
