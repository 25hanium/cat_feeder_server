from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class Cat(Base):
    __tablename__ = "cats"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    tag_id = Column(String(50), unique=True)
    feedings = relationship("FeedingLog", back_populates="cat")

class FeedingLog(Base):
    __tablename__ = "feeding_logs"
    id = Column(Integer, primary_key=True, index=True)
    cat_id = Column(Integer, ForeignKey("cats.id"))
    weight = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    cat = relationship("Cat", back_populates="feedings")

class FeedingLimit(Base):
    __tablename__ = "feeding_limits"
    id = Column(Integer, primary_key=True, index=True)
    cat_id = Column(Integer, ForeignKey("cats.id"))
    max_amount_per_meal = Column(Float)
    max_meals_per_day = Column(Integer)
