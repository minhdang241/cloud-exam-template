from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings
from .base_class import PostgresBase

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True
)

# each instance of this class will be the database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Later we will inherit from this class to create each of the database models or classes (the ORM models)
Base = declarative_base(cls=PostgresBase)
