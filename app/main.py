from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import SensorData
from .schemas import SensorDataCreate, SensorDataResponse
import os
import json

app = FastAPI()
SensorData.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

LOG_FILE = "feeding_log.json"

@app.post("/log", response_model=SensorDataResponse)
def create_log(data: SensorDataCreate, db: Session = Depends(get_db)):
    # 저장
    db_data = SensorData(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)

    # JSON 로그
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    logs.append(data.dict())
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)

    return db_data

@app.get("/log", response_model=list[SensorDataResponse])
def get_logs(db: Session = Depends(get_db)):
    return db.query(SensorData).order_by(SensorData.id.desc()).all()
