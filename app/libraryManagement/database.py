from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database configuration
engine = create_engine(
    'sqlite:///library.db',
    echo=False,
    connect_args={"check_same_thread": False}
)

# Create a configured "Session" class
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create a Base class for declarative class definitions
Base = declarative_base()