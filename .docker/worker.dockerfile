FROM python:3.8 AS base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app


RUN pip install --upgrade pip
RUN pip install poetry
ADD . /app
EXPOSE 8000
RUN poetry install
CMD ["poetry", "run", "celery", "-A", "app.services.worker", "worker", "--loglevel=debug", "--beat"]