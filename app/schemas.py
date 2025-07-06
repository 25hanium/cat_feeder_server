from pydantic import BaseModel
from datetime import datetime

class FeedingLogCreate(BaseModel):
    tag_id: str
    weight: float

class FeedingLimitUpdate(BaseModel):
    tag_id: str
    max_amount_per_meal: float
    max_meals_per_day: int

class FeedingLogResponse(BaseModel):
    cat_id: int
    weight: float
    timestamp: datetime

    class Config:
        orm_mode = True
