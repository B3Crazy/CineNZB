from libraryManagement.database import Base, engine
from libraryManagement.models import NZB

# Create all tables
Base.metadata.create_all(bind=engine)