from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

from backend.config import settings


from backend.utils.paths import DATABASE_DIR

database_directory = DATABASE_DIR
database_directory.mkdir(parents=True, exist_ok=True)


engine = create_engine(
	settings.database_url,
	connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=engine
)


class Base(DeclarativeBase):
	pass


def get_db():
	db = SessionLocal()

	try:
		yield db

	finally:
		db.close()