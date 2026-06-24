from libraryManagement.database import SessionLocal
from libraryManagement.models import NZB

def import_nzbs(nzb_list):
    db = SessionLocal()
    try:
        for nzb in nzb_list:
            existing_nzb = db.query(NZB).filter_by(filename=nzb['filename']).first()
            if not existing_nzb:
                new_nzb = NZB(filename=nzb['filename'], path=nzb['path'])
                db.add(new_nzb)
        db.commit()
    finally:
        db.close()