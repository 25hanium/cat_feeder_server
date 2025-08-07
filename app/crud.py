from sqlalchemy.orm import Session
from models import FeedingLog
from schemas import FeedingLogCreate

def create_log(db: Session, log: FeedingLogCreate):
    db_log = FeedingLog(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def get_latest_log(db: Session):
    return db.query(FeedingLog).order_by(FeedingLog.timestamp.desc()).first()
