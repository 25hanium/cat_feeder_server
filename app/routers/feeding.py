from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/log")
def create_log(data: schemas.FeedingLogCreate, db: Session = Depends(get_db)):
    cat = db.query(models.Cat).filter(models.Cat.tag_id == data.tag_id).first()
    if not cat:
        cat = models.Cat(name=f"Cat-{data.tag_id}", tag_id=data.tag_id)
        db.add(cat)
        db.commit()
        db.refresh(cat)

    log = models.FeedingLog(cat_id=cat.id, weight=data.weight)
    db.add(log)
    db.commit()
    return {"message": "Feeding logged"}

@router.post("/limit")
def set_limit(data: schemas.FeedingLimitUpdate, db: Session = Depends(get_db)):
    cat = db.query(models.Cat).filter(models.Cat.tag_id == data.tag_id).first()
    if not cat:
        raise HTTPException(status_code=404, detail="Cat not found")

    limit = db.query(models.FeedingLimit).filter(models.FeedingLimit.cat_id == cat.id).first()
    if not limit:
        limit = models.FeedingLimit(
            cat_id=cat.id,
            max_amount_per_meal=data.max_amount_per_meal,
            max_meals_per_day=data.max_meals_per_day
        )
    else:
        limit.max_amount_per_meal = data.max_amount_per_meal
        limit.max_meals_per_day = data.max_meals_per_day

    db.add(limit)
    db.commit()
    return {"message": "Feeding limit set"}
