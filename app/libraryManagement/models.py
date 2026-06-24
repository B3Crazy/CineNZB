from sqlalchemy import Column, Integer, String, DateTime
from libraryManagement.database import Base
from datetime import datetime

class NZB(Base):
    __tablename__ = 'nzbs'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    path = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    