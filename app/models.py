from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)

class Cat(Base):
    __tablename__ = "cats"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)
    gender = Column(String(10))
    food_favor = Column(String(50))
    feeding_time = Column(DateTime)
    feeding_amount = Column(Integer)
    tag_id = Column(String(50), unique=True)
    
    feedings = relationship("FeedingLog", back_populates="cat")

class FeedingLog(Base):
    __tablename__ = "feeding_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    cat_id = Column(Integer, ForeignKey("cats.id"))
    weight = Column(Float)
    timestamp_start = Column(DateTime, default=datetime.utcnow)
    timestamp_end = Column(DateTime, default=datetime.utcnow)
    feeding_amount = Column(Integer)
    left_amount = Column(Integer)
    file_path = Column(String(100))
    
    cat = relationship("Cat", back_populates="feedings")

class FeedingInfo(Base):
    __tablename__ = "feeding_info"
    
    id = Column(Integer, primary_key=True, index=True)
    feeding_id = Column(Integer, ForeignKey("feeding_logs.id"))
    cat_id = Column(Integer, ForeignKey("cats.id"))
    behavior = Column(String(50))

class FeedingLimit(Base):
    __tablename__ = "feeding_limits"
    id = Column(Integer, primary_key=True, index=True)
    cat_id = Column(Integer, ForeignKey("cats.id"))
    max_amount_per_meal = Column(Float)
    max_meals_per_day = Column(Integer)

class FeederState(Base):
    __tablename__ = "feeder_state"
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    left_amount = Column(Integer)
