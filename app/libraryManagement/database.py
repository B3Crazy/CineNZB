from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

config_dir = os.environ.get('CONFIG_DIR', '/config')
os.makedirs(config_dir, exist_ok=True)

db_path = os.path.join(config_dir, 'library.db')

# Database configuration
engine = create_engine(
    f'sqlite:///{db_path}',
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