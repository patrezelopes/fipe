from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine

from app.deps import get_settings
from app.models.base import Base

config = context.config
config.set_main_option(
    "sqlalchemy.url", get_settings().database_url,
)  # overwrite alembic.ini

fileConfig(config.config_file_name)


target_metadata = Base.metadata


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    url = config.get_main_option("sqlalchemy.url")
    connectable = create_engine(url)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
