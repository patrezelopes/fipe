FROM python:3.8 AS base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app


RUN pip install --upgrade pip
RUN pip install poetry
ADD . /app
EXPOSE 8000
RUN poetry install
CMD ["poetry", "run", "uvicorn", "asgi:application", "--host", "0.0.0.0", "--port", "8000"]