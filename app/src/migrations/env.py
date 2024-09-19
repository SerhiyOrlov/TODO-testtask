import asyncio
from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import pool
from alembic import context
from config.config import DATABASE_URL
from auth.database import AuthBase

# Alembic Config object
config = context.config

# Configure logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Add your model's MetaData object here
target_metadata = AuthBase.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_async_engine(
        DATABASE_URL, 
        poolclass=pool.NullPool, 
        echo=True  # For debugging purposes; remove or set to False in production
    )

    async with connectable.connect() as connection:
        # Run migrations in async context
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata
    )

    with context.begin_transaction():
        context.run_migrations()

# Run the migrations
if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
