from fastapi import FastAPI
from .database import Base, engine
from .routers import feeding

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(feeding.router, prefix="/feeding", tags=["Feeding"])

@app.post("/api/logs", response_model=schemas.FeedingLogResponse)
def create_log(log: schemas.FeedingLogCreate, db: Session = Depends(get_db)):
    return crud.create_log(db, log)

@app.get("/api/logs/latest", response_model=schemas.FeedingLogResponse)
def latest_log(db: Session = Depends(get_db)):
    return crud.get_latest_log(db)

@app.post("/log")
async def log_feeding(data: FeedingLog):
    # 여기에 DB 저장 로직 삽입 가능
    print(f"✅ Received data from RPi: {data}")

    # 예시: DB 저장 함수
    # insert_log_to_db(data.cat_id, data.feeding_time, data.food_amount, data.behavior_notes)

    return {"status": "ok", "message": "Feeding log stored successfully", "data": data}
