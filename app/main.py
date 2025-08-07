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
