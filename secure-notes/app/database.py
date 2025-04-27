# secure-notes/app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Get the database URL from environment variables (with a default fallback)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/secure_notes")

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a configured \"Session\" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

# Dependency function to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
