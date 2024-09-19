import os

DB_CONFIG = {
	"DB_HOST": os.environ.get('POSTGRES_HOST'),
	"DB_PORT": os.environ.get('POSTGRES_PORT'),
	"DB_NAME": os.environ.get('POSTGRES_DB'),
	"DB_USER": os.environ.get('POSTGRES_USER'),
	"DB_PASS": os.environ.get('POSTGRES_PASSWORD'),
}

DATABASE_URL = f"postgresql+asyncpg://{DB_CONFIG['DB_USER']}:{DB_CONFIG['DB_PASS']}@{DB_CONFIG['DB_HOST']}:{DB_CONFIG['DB_PORT']}/{DB_CONFIG['DB_NAME']}"
