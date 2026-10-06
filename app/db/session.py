from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Create a SQLAlchemy engine using the database URL from the settings
engine = create_engine(
    settings.DATABASE_URL,
)

# The sessionmaker function is used to create a new session factory that will be used to create database sessions.
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

# The get_db function is a dependency that can be used in FastAPI routes to provide a database session.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()