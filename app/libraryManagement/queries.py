from libraryManagement.database import SessionLocal
from libraryManagement.models import NZB
from libraryManagement.scanner import scan_library
import os

def get_all():
    db = SessionLocal()
    try:
        nzbs = db.query(NZB).all()
    finally:
        db.close()
    return nzbs
