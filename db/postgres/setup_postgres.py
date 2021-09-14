from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from .base_class import PostgresBase
engine = create_engine(
            settings.SQLALCHEMY_DATABASE_URL,
                pool_pre_ping=True
                )
label_engine = create_engine(
            settings.SQLALCHEMY_LABEL_DATABASE_URL,
                pool_pre_ping=True
                )
# each instance of this class will be the database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
LabelSession = sessionmaker(
            autocommit=False, autoflush=False, bind=label_engine)
# Later we will inherit from this class to create each of the database models or classes (the ORM models)
Base = declarative_base(cls=PostgresBase)
